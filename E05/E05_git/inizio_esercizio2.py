import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def leggi_file(nome):
    tabella = pd.read_csv(nome)

    return tabella


#import dei dati
tabella0 = leggi_file('/home/martina/MCF/Metodi-computazionali-per-la-fisica/E05/hit_times_M0.csv')
tabella1 = leggi_file('/home/martina/MCF/Metodi-computazionali-per-la-fisica/E05/hit_times_M1.csv')
tabella2 = leggi_file('/home/martina/MCF/Metodi-computazionali-per-la-fisica/E05/hit_times_M2.csv')
tabella3 = leggi_file('/home/martina/MCF/Metodi-computazionali-per-la-fisica/E05/hit_times_M3.csv')


#istogramma dei tempi del modulo 0
n, bins, p = plt.hist(tabella0['hit_time'], bins= 50, color= 'blue')
plt.xlabel('Tempi [ns]')
plt.ylabel('Numero di eventi')
plt.title('Istogramma dei tempi del modulo 0')
plt.show()

print(tabella0.shape)
#istogramma della differenza dei tempi del modulo 0
differenze = np.diff(tabella0['hit_time'].values)
print(differenze)


mask = differenze > 0

diff_mask = differenze[mask]

n1, bins1, p1 = plt.hist(np.log10(diff_mask), bins= 50, color = 'orange')
plt.xlabel('$log_{10}(\Delta t)$')
plt.ylabel('Numero di eventi')
plt.title('Istogramma del $log_{10}(\Delta t)$ del modulo 0')
plt.show()




