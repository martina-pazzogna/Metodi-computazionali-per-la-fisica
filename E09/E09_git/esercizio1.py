import numpy as np
import pandas as pd
from scipy import constants, fft
import matplotlib.pyplot as plt
from scipy import optimize

#funzione per leggere i file
def leggi(nome_file):
    dati = pd.read_csv(nome_file, delimiter = ',')
    return dati

#lettura dei dati
dati1 = leggi('data_sample1.csv')
dati2 = leggi('data_sample2.csv')
dati3 = leggi('data_sample3.csv')

#grafico dei tre segnali in ingresso
plt.plot(dati1['time'], dati1['meas'], color = 'blue', label = 'Segnale 1')
plt.plot(dati2['time'], dati2['meas'], color = 'orange', label = 'Segnale 2')
plt.plot(dati3['time'], dati3['meas'], color = 'red', label = 'Segnale 3')
plt.xlabel('Tempo [s]')
plt.ylabel('Ampiezza del segnale [U.A.]')
plt.legend()
plt.title('Grafico che mostra i tre segnali in ingresso')
plt.show()

#calcolo della trasformata di Fourier dei tre segnali in ingresso
trasf_1 = fft.rfft(np.array(dati1['meas']))
trasf_2 = fft.rfft(np.array(dati2['meas']))
trasf_3 = fft.rfft(np.array(dati3['meas']))


dt = dati1['time'][1] - dati1['time'][0]
frequenze= fft.rfftfreq(len(dati1['time']), dt)

#calcolo e grafico della potenza dei tre segnali
trasformate = np.array([trasf_1, trasf_2, trasf_3])
pot = []
for i in range(3):
    pot.append(np.absolute(trasformate[i])**2)
potenze = np.array(pot)

plt.plot(frequenze, potenze.T ,  label = ['Segnale 1', 'Segnale 2', 'Segnale 3'])
plt.xlabel('Frequenze [Hz]')
plt.ylabel('Potenza [U.A.]')
plt.xscale('log')
plt.yscale('log')
plt.title('Grafico dello spettro di potenza dei tre segnali')
plt.legend()
plt.show()

#fit dei tre spettri di potenza
def funzione_fit(x , b, A):
    return np.log10(A) - b * x

par = []
var = []
mask = frequenze > 0
for i in range(3):
    params, params_covariance = optimize.curve_fit(funzione_fit, np.log10(frequenze[mask]), np.log10(potenze[i][mask]), p0 = [0, 5] )
    par.append(params)
    var.append(np.sqrt(params_covariance.diagonal()))
parametri = np.array(par)
varianza = np.array(var)

print(parametri)
#grafico dei risultati dei fit

fig, axs = plt.subplots(1, 3, figsize = (15,4))

axs[0].plot(np.log10(frequenze[mask]), np.log10(potenze[0][mask]), 'o', color = 'orange')
axs[0].plot(np.log10(frequenze[mask]), funzione_fit(np.log10(frequenze[mask]), parametri[0][0], parametri[0][1]), color = 'black')
axs[0].set_xlabel('Frequenza [Hz]')
axs[0].set_ylabel('Potenza [U.A.]')
axs[0].set_title('Fit dello spettro di potenza del segnale 1')

axs[1].plot(np.log10(frequenze[mask]), np.log10(potenze[1][mask]), 'o', color = 'red')
axs[1].plot(np.log10(frequenze[mask]), funzione_fit(np.log10(frequenze[mask]), parametri[1][0], parametri[1][1]), color = 'black')
axs[1].set_xlabel('Frequenza [Hz]')
axs[1].set_ylabel('Potenza [U.A.]')
axs[1].set_title('Fit dello spettro di potenza del segnale 2')

axs[2].plot(np.log10(frequenze[mask]), np.log10(potenze[2][mask]), 'o', color = 'blue')
axs[2].plot(np.log10(frequenze[mask]), funzione_fit(np.log10(frequenze[mask]), parametri[2][0], parametri[2][1]), color = 'black')
axs[2].set_xlabel('Frequenza [Hz]')
axs[2].set_ylabel('Potenza [U.A.]')
axs[2].set_title('Fit dello spettro di potenza del segnale 3')
plt.tight_layout()
plt.show()