import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--velocita", "-v", help = "Mostra il grafico della velocità in funzione del tempo", action = "store_true")
parser.add_argument("--distanza", "-d", help ="Mostra il grafico della distanza in funzione del tempo", action = "store_true")
args= parser.parse_args()


dati = pd.read_csv('vel_vs_time.csv')

#grafico dei dati
plt.figure()
plt.plot( dati['t'], dati['v'])
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')
plt.title('Grafico della velocità in funzione del tempo')
plt.grid('True')
if args.velocita:
    plt.show()
plt.close()


#calcolo della distanza percorsa in totale
d_tot = integrate.simpson(dati['v'], x = dati['t'])
print('La distanza percorsa in totale è ', d_tot, "metri")

#calcolo della distanza percorsa in funzione del tempo
dist = []

for i in range(len(dati['t'])):
    d = integrate.simpson(y = dati['v'][:i+1], x = dati['t'][:i+1])
    dist.append(d)

distanze = np.array(dist)
print("Array delle distanze percorse : ", distanze)

#grafico della distanza percorsa in funzione del tempo
plt.figure()
plt.plot(dati['t'], distanze)
plt.xlabel('t [s]')
plt.ylabel('d [m]')
plt.title('Grafico della distanza percorsa in funzione del tempo')
plt.grid('True')
if args.distanza:
    plt.show()


