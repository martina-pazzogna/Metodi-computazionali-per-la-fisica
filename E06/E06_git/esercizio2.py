import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( "--sesta", help = "Mostra il grafico con potenziale di ordine 6", action = "store_true")
parser.add_argument("--quad", help ="Mostra il grafico con potenziale di ordine 2", action = "store_true")
args= parser.parse_args()


m = 1
k = 0.1

#funzione che definisce il potenziale
def potenziale(x, n):
    return k * x**n


#funzione che calcola il periodo in funzione di x0
def periodo(x0, n):
    intervallo_integrazione = np.linspace(0, x0, 1000, endpoint = False)
    integranda = 1/np.sqrt(potenziale(x0, n) - potenziale(intervallo_integrazione, n))
    return np.sqrt(8 * m) * integrate.simpson(y = integranda, x = intervallo_integrazione)

#grafico del periodo in funzione di xo- n=6
x = np.linspace(0.1,6, 200)
y6 = [periodo(val, 6) for val in x]

plt.figure()
plt.plot(x,y6)
plt.xlabel('x0 [m]')
plt.ylabel('T [s]')
plt.grid('True')
plt.title('Grafico del periodo in funzione di x0, con potenziale del tipo V(x)= kx^6')
if args.sesta:
    plt.show()
plt.close()

#grafico del periodo in funzione di x0 - n=2
y2 = [periodo(val, 2) for val in x]
print(y2)

plt.figure()
plt.plot(x,y2)
plt.xlabel('x0 [m]')
plt.ylabel('T [s]')
plt.grid('True')
plt.title('Grafico del periodo in funzione di x0, con potenziale del tipo V(x)= kx^2')
#plt.ylim(13.6,13.7)
if args.quad:
    plt.show()
plt.close()
