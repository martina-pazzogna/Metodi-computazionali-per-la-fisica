import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

#import dei dati
tabella_dati = pd.read_csv('Jpsimumu.csv')

#calcolo della massa invariante per ogni evento
def massa_invariante(e1, e2, p1x, p1y, p1z, p2x, p2y, p2z):

    """
    variabili: energie e componenti dell'impulso delle due particelle

    --------
    return : massa invariante per un decadimento a due copri

    """

    t1 = (e1 + e2)**2
    t2 = (p1x + p2x)**2 + (p1y + p2y)**2 + (p1z + p2z)**2

    return np.sqrt(t1 - t2)
lista= []
for i in range(len(tabella_dati)):
    m = massa_invariante(tabella_dati['E1'][i], tabella_dati['E2'][i], tabella_dati['px1'][i], tabella_dati['py1'][i], tabella_dati['pz1'][i], tabella_dati['px2'][i], tabella_dati['py2'][i], tabella_dati['pz2'][i])
    lista.append(m)

masse = np.array(lista)

#istogramma delle masse
n, bins, p = plt.hist(masse, bins = 500, color = 'orange')
plt.xlabel('Massa invariante [GeV]')
plt.ylabel('Numero di eventi')
plt.title('Istogramma della massa invariante')
plt.show()

n1, bins1, p1 = plt.hist(masse, bins= 500, range = (2.95, 3.25), color = 'purple')
plt.xlabel('Massa invariante [GeV]')
plt.ylabel('Numero di eventi')
plt.title('Istogramma della massa invariante nella regione intorno al picco')
plt.show()


#fit con gaussiana singola
def fg1(x, A, mu, a, p1, p0):

    """
    parametri: costante di normalizzazione A, media mu, deviazione standard a, coeff ang p1, intercetta p0
    variabile: x

    --------
    
    return: somma di una gaussiana e un polinomio di primo grado

    """

    g = A*np.exp((-(x-mu)**2)/(2* a**2))
    pol = p1*x + p0

    return g + pol

centri_bin = 0.5 * (bins1[:-1] + bins1[1:])
mask = n1 > 0

pstart = np.array([350, 3.10, 0.10, 1, 1])
params, params_covariance = optimize.curve_fit(fg1, centri_bin[mask], n1[mask], sigma= np.sqrt(n1[mask]), p0 = pstart)
print('Parametri con gaussiana singola=', params)
print("Incertezza sui parametri con gaussiana singola=", np.sqrt(params_covariance.diagonal()))

#grafico con curva di fit con gaussiana singola
y_array = fg1(centri_bin, params[0], params[1], params[2], params[3], params[4])
scarti = n1 - y_array
scarti_err = scarti[mask]/np.sqrt(n1[mask])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize= (13,6))
n1, bins1, p1 = ax1.hist(masse, bins= 500, range = (2.95, 3.25), color = 'purple', label= 'Dati')
ax1.plot(centri_bin, y_array, label = 'Curva ottenuta dal fit-gaussiana singola')
ax1.legend()
ax1.set_xlabel('Massa invariante [GeV]')
ax1.set_ylabel('Numero di eventi')
ax1.set_title('Confronto tra i dati e la curva di fit con gaussiana singola')

ax2.plot(centri_bin, scarti)
ax2.set_xlabel("Massa invariante [GeV]")
ax2.set_ylabel("Scarto tra i dati e fit con gaussiana singola")
ax2.set_title("Scarto tra i dati e il fit con gaussiana singola")

plt.show()

plt.plot(centri_bin[mask], scarti_err)
plt.xlabel("Massa invariante [GeV]")
plt.ylabel("Scarto tra i dati e fit diviso per l'errore con gaussiana singola")
plt.title("Scarto tra i dati e il fit diviso per l'errore con gaussiana singola")
plt.show()

#calcolo del chi-quadro per fit con gaussiana singola
y_fit = fg1(centri_bin[mask], params[0], params[1], params[2], params[3], params[4])
chi2 = np.sum((y_fit - n1[mask])**2/n1[mask])
grad_lib = len(centri_bin[mask]) - len(params)

chi2_rid = chi2/ grad_lib
print("Il chi2 ridotto facendo il fit con gaussiana singola è ", chi2_rid)

#fit con gaussiana doppia
def fg2(x, A1, mu1, a1, A2, mu2, a2, p1, p0):

    """
    parametri: costante di normalizzazione A, media mu, deviazione standard a per entrambe le gaussiane, coeff ang p1, intercetta p0
    variabile: x

    --------
    
    return: somma di due gaussiane e un polinomio di primo grado

    """

    g1 = A1*np.exp((-(x-mu1)**2)/(2* a1**2))
    g2 = A2*np.exp((-(x-mu2)**2)/(2* a2**2))
    pol = p1*x + p0

    return g1 + g2 + pol

params1, params_covariance1 = optimize.curve_fit(fg2, centri_bin[mask], n1[mask], sigma= np.sqrt(n1[mask]))
print('Parametri con gaussiana doppia=', params1)
print("Incertezza sui parametri conn gaussiana doppia=", np.sqrt(params_covariance1.diagonal()))

#grafico con curva di fit con gaussiana doppia
y_array1 = fg2(centri_bin, params1[0], params1[1], params1[2], params1[3], params1[4], params1[5], params1[6], params1[7])
scarti1 = n1 - y_array1
scarti_err1 = scarti[mask]/np.sqrt(n1[mask])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize= (13,6))
n1, bins1, p1 = ax1.hist(masse, bins= 500, range = (2.95, 3.25), color = 'purple', label= 'Dati')
ax1.plot(centri_bin, y_array1, label = 'Curva ottenuta dal fit con gaussiana doppia')
ax1.legend()
ax1.set_xlabel('Massa invariante [GeV]')
ax1.set_ylabel('Numero di eventi')
ax1.set_title('Confronto tra i dati e la curva di fit con gaussiana doppia')

ax2.plot(centri_bin, scarti1)
ax2.set_xlabel("Massa invariante [GeV]")
ax2.set_ylabel("Scarto tra i dati e fit con gaussiana doppia")
ax2.set_title("Scarto tra i dati e il fit con gaussiana doppia")

plt.show()

plt.plot(centri_bin[mask], scarti_err1)
plt.xlabel("Massa invariante [GeV]")
plt.ylabel("Scarto tra i dati e fit diviso per l'errore con gaussiana doppia")
plt.title("Scarto tra i dati e il fit diviso per l'errore con gaussiana doppia")
plt.show()

#calcolo del chi-quadro per fit con gaussiana doppia
y_fit1 = fg2(centri_bin[mask], params1[0], params1[1], params1[2], params1[3], params1[4], params1[5], params1[6], params1[7])
chi21 = np.sum((y_fit1 - n1[mask])**2/n1[mask])
grad_lib = len(centri_bin[mask]) - len(params)

chi2_rid1 = chi21/ grad_lib
print("Il chi2 ridotto con gaussiana doppia è ", chi2_rid1)







