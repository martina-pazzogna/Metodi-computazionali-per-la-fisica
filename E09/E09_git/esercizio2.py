import numpy as np
import pandas as pd
from scipy import constants, fft
import matplotlib.pyplot as plt
from scipy import optimize

#funzione per leggere i file
def leggi(nome_file):
    dati = pd.read_csv(nome_file, delimiter = ',')
    return dati

#lettura dei file
dati1 = leggi('4FGL_J2202.7+4216_weekly_9_15_2023_mcf.csv')
dati2 = leggi('4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv')
dati3 = leggi('4FGL_J2253.9+1609_weekly_9_15_2023_mcf.csv')

#grafico dei dati (Fluss vs Giorno Giuliano)
plt.plot(dati1['Julian Date'], dati1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], label='Sorgente 1')
plt.plot(dati2['Julian Date'], dati2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], label='Sorgente 2')
plt.plot(dati3['Julian Date'], dati3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], label='Sorgente 3')
plt.xlabel('Data [Giorno giuliano]')
plt.ylabel('Flusso [fotoni cm^-2 s^-1]')
plt.title('Grafico del flusso delle tre sorgenti')
plt.show()

#grafico dei dati in tre pannelli separati
fig, ax = plt.subplots(1,3, figsize= (12,5))

ax[0].plot(dati1['Julian Date'], dati1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], 'o', color= 'orange')
ax[0].set_xlabel('Data [Giorno giuliano]')
ax[0].set_ylabel('Flusso [fotoni cm^-2 s^-1]')
ax[0].set_title('Flusso della sorgente 1')

ax[1].plot(dati2['Julian Date'], dati2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], 'o', color= 'green')
ax[1].set_xlabel('Data [Giorno giuliano]')
ax[1].set_ylabel('Flusso [fotoni cm^-2 s^-1]')
ax[1].set_title('Flusso della sorgente 2')

ax[2].plot(dati2['Julian Date'], dati2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], 'o', color= 'purple')
ax[2].set_xlabel('Data [Giorno giuliano]')
ax[2].set_ylabel('Flusso [fotoni cm^-2 s^-1]')
ax[2].set_title('Flusso della sorgente 3')

plt.show()

#creazione dizionario: ciascun valore contiene le colonne del tempo e del flusso di ciascuna sorgente
sorg1 = np.array([np.array(dati1['Julian Date']), np.array(dati1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'])])
sorg2 = np.array([np.array(dati2['Julian Date']), np.array(dati2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'])])
sorg3 = np.array([np.array(dati3['Julian Date']), np.array(dati3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'])])

dizionario = {"Sorgente 1": sorg1,
"Sorgente 2": sorg2,
"Sorgente 3": sorg3
}

#calcolo della trasformata di fourier
for k in list(dizionario.keys())[:3]:
    dt = dizionario[k][0][1] - dizionario[k][0][0]
    trasformata = fft.rfft(dizionario[k][1])
    frequenza = fft.rfftfreq(len(dizionario[k][1]), dt)
    dizionario['Trasformata ' + k] = np.array([trasformata, frequenza])

#grafico degli spettri di potenza
fig, ax = plt.subplots(1,3, figsize = (14,5))

ax[0].plot(dizionario['Trasformata Sorgente 1'][1], np.absolute(dizionario['Trasformata Sorgente 1'][0])**2, 'o', color = 'green' )
ax[0].set_xlabel('Frequenze [1/giorno giuliano]-log scale')
ax[0].set_ylabel('Potenza [U.A.]-log scale')
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].set_title('Spettro di potenza della sorgente 1')

ax[1].plot(dizionario['Trasformata Sorgente 2'][1], np.absolute(dizionario['Trasformata Sorgente 2'][0])**2,'o' ,color = 'purple' )
ax[1].set_xlabel('Frequenze [1/giorno giuliano]-log scale')
ax[1].set_ylabel('Potenza [U.A.]- log scale')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_title('Spettro di potenza della sorgente 2')

ax[2].plot(dizionario['Trasformata Sorgente 3'][1], np.absolute(dizionario['Trasformata Sorgente 3'][0])**2, 'o', color = 'pink' )
ax[2].set_xlabel('Frequenze [1/giorno giuliano]-log scale')
ax[2].set_ylabel('Potenza [U.A.]-log scale')
ax[2].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_title('Spettro di potenza della sorgente 3')

plt.show()


#fit per stimare l'andamento degli spettri di potenza
def funzione_fit(x , b, A):
    return np.log10(A) - b * x

par = []
var = []

for k in list(dizionario.keys())[-3:]:
    f = dizionario[k][1]
    p = np.absolute(dizionario[k][0])**2
    mask = (f>0) & (f != 1)
    params, params_covariance = optimize.curve_fit(funzione_fit, np.log10(f[mask]), np.log10(p[mask]), p0 = [0, 5] )
    par.append(params)
    var.append(np.sqrt(params_covariance.diagonal()))
parametri = np.array(par)
varianza = np.array(var)

#grafici dei fit

fig, axs = plt.subplots(1,3, figsize= (14,5))

for ax, k, i in zip(axs, list(dizionario.keys())[-3:], range(3)):
    f = dizionario[k][1]
    mask = (f>0) & (f != 0)
    x = np.log10(f[mask])
    y1 = np.log10(np.absolute(dizionario[k][0][mask])**2)
    y2 = funzione_fit(x, parametri[i][0], parametri[i][1])
    ax.plot(x, y1, 'o', label = 'Dati')
    ax.plot(x, y2, label = 'Fit')
    ax.set_xlabel('Frequenza [1/giorno giuliano]- log scale')
    ax.set_ylabel('Potenza [U.A.]- log scale')
    ax.set_title('Fit della potenza della sorgente ' + str(i+1))
    ax.legend()

plt.show()

#grafico dei tre spettri di potenza sovrapposti
fig, ax = plt.subplots(figsize = (6,5))
for k, i in zip(list(dizionario.keys())[-3:], range(3)):
    f = dizionario[k][1]
    mask = (f>0) & (f != 1)
    x = f[mask]
    y= np.absolute(dizionario[k][0][mask])**2
    ax.plot(x,y, 'o', label = 'Sorgente ' + str(i+1))
    ax.set_xlabel('Frequenza [1/giorno giuliano]-log scale')
    ax.set_ylabel('Potenza [U.A.] -log scale')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend()
    ax.set_title('Potenza delle tre sorgenti')

plt.show()


#grafico dei tre spettri di potenza normalizzati ai corrispettivi coefficienti di ordine 0
fig, ax = plt.subplots(figsize = (6,5))
for k, i in zip(list(dizionario.keys())[-3:], range(3)):
    f = dizionario[k][1]
    mask = (f>0) & (f != 1)
    x = f[mask]
    y= (np.absolute(dizionario[k][0][mask])**2)/parametri[i][1]
    ax.plot(x,y, 'o', label = 'Sorgente ' + str(i+1))
    ax.set_xlabel('Frequenza [1/giorno giuliano]-log scale')
    ax.set_ylabel('Potenza [U.A.] -log scale')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend()
    ax.set_title('Potenza delle tre sorgenti normalizzata al coefficiente di ordine 0')

plt.show()

#filtro delle frequenze
filtro1 = dizionario['Trasformata Sorgente 1'][1] < 0.005
filtro2 = dizionario['Trasformata Sorgente 2'][1] < 0.004
filtro3 = dizionario['Trasformata Sorgente 3'][1] < 0.003

flusso_fil = []
flusso_compl = []
filtri = [filtro1, filtro2, filtro3]
for k, i in zip(list(dizionario.keys())[-3:], range(3)):
    trasf_filtr = dizionario[k][0].copy()
    trasf_filtr[filtri[i]] = 0
    trasf_compl = dizionario[k][0].copy()
    trasf_compl[~filtri[i]] = 0

    filtrato = fft.irfft(trasf_filtr, n = len(dizionario['Sorgente ' + str(i+1)][0]))
    complementare = fft.irfft(trasf_compl, n = len(dizionario['Sorgente ' + str(i+1)][0]))

    flusso_fil.append(filtrato)
    flusso_compl.append(complementare)

filtrati = np.array(flusso_fil, dtype = object)
complementari = np.array(flusso_compl, dtype = object)

#grafici dei dati filtrati, sovrapposti a quelli non filtrati
fig, axs = plt.subplots(1,3, figsize= (15,5))
for ax, k, i in zip(axs, list(dizionario.keys())[:3], range(3)):
    x = dizionario[k][0]
    y1 = dizionario[k][1]
    y2 = filtrati[i]
    ax.plot(x, y1, label = 'Flusso non filtrato', color = 'purple')
    ax.plot(x, y2, label = 'Flusso filtrato', color = 'black')
    ax.set_xlabel('Data [Giorno giuliano]')
    ax.set_ylabel('Flusso [fotoni cm^-2 s^-1]')
    ax.set_title('Eliminazione alte frequenze sorgente ' + str(i+1))
    ax.legend()

plt.show()

