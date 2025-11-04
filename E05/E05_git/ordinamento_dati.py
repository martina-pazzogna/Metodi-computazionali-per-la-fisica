import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append('.')

import reco
import inizio_esercizio2

#creazione degli array
def creazione_array(nome):
    dati = inizio_esercizio2.leggi_file(nome)
    
    lista = []
    for index, row in dati.iterrows():
        riga = reco.Hit(row['mod_id'], row['det_id'], row['hit_time'])
        lista.append(riga)

    return np.array(lista)

#import dei dati
array_0 = creazione_array('/home/martina/MCF/Metodi-computazionali-per-la-fisica/E05/hit_times_M0.csv')
array_1 = creazione_array('/home/martina/MCF/Metodi-computazionali-per-la-fisica/E05/hit_times_M1.csv')
array_2 = creazione_array('/home/martina/MCF/Metodi-computazionali-per-la-fisica/E05/hit_times_M2.csv')
array_3 = creazione_array('/home/martina/MCF/Metodi-computazionali-per-la-fisica/E05/hit_times_M3.csv')

#dati totali ordinati
totale = np.concatenate((array_0, array_1, array_2, array_3))
ordinati = np.sort(totale)

#istrogramma
tempi = np.array([h.id_rivelazione for h in ordinati])
x = np.diff(tempi)
mask = x>0
x_m = x[mask]
n, bins, p = plt.hist(np.log10(x_m), bins= 100, color = 'orange')
plt.xlabel('$log_{10}(\Delta t)$')
plt.ylabel('Numero di eventi')
plt.title('Istogramma del $log_{10}(\Delta t)$ del modulo 0')
plt.show()



