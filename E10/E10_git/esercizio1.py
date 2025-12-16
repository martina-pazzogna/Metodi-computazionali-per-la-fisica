import numpy as np
import matplotlib.pyplot as plt

#definizione della forma funzionale della distribuzione
def distribuzione(x):
    """
    Restituisce la funzione 3/1000 x^2

    """
    return 3/1000 * x**2

#costruzione della distibuzione mediante il metodo Hit or Miss

n = 100000 #numero di estrazioni
x_gen = np.random.uniform(low = 0, high = 10, size = n)
y_gen = np.random.random(n)

mask_distr = y_gen <= distribuzione(x_gen) #maschera per selezionare x

x_distr = x_gen[mask_distr]

#istogramma della distribuzione
plt.hist(x_gen, bins = 100, range = (0,10), alpha = 0.7, color = 'pink', label = 'Valori di x generati')
plt.hist(x_distr, bins = 100, range = (0,10), color = 'purple', label = 'Valori di x selezionati')
plt.xlabel('x')
plt.ylabel('N estrazioni')
plt.title('Istogramma della distribuzione ottenuta- Hit or Miss')
plt.legend(loc = 'best')
plt.show()

#costruzione della distribuzione con il metodo della cumulativa

def cumulativa_inversa(x):
    """
    funzione che restituisce l'inversa della funzione integrale della distribuzione
    c(x) = 1/1000 x^3
    c^-1(x) = (1000 z)^1/3
    """
    return (1000 * x)**(1/3)

y_gen_2 = np.random.random(n) #array di valori estratti
x_distr_2 = cumulativa_inversa(y_gen_2)

#istogramma della distribuzione
plt.hist(x_distr_2, bins = 100, range = (0,10), color = 'purple', label = 'Valori di x selezionati')
plt.hist(y_gen, bins = 100, range = (0,10), alpha = 0.7, color = 'pink', label = 'Valori di y generati')
plt.xlabel('x')
plt.ylabel('N estrazioni')
plt.title('Istogramma della distribuzione ottenuta- Cumulativa inversa')
plt.legend(loc = 'best')
plt.show()

#istogramma di confronto
plt.hist(x_distr, bins = 100, range = (0,10), color = 'purple', label = 'Metodo Hit or Miss')
plt.hist(x_distr_2, bins = 100, range = (0,10), color = 'pink', alpha= 0.6, label = 'Metodo cumulativa inversa')
plt.xlabel('x')
plt.ylabel('N estrazioni')
plt.title('Confronto tra le due distribuzioni ottenute')
plt.legend(loc = 'best')
plt.show()

