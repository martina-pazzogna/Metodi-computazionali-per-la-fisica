import sys
sys.path.append('.')
import somme

n_100 = somme.somma(100)
print('La somma dei primi 100 numeri naturali è ', n_100)

n_10 = somme.somma_radici(10)
print('La somma delle radici dei primi 10 numeri naturali è ', n_10)

n2, n3 = somme.somma_prodotto(10)
print("La somma e il prodotto dei primi 10 numeri naturali sono ", n2, ",", n3)

n4= somme.somma_alpha(10,2)
print("La somma dei quadrati dei primi 10 numeri naturali è ", n4)