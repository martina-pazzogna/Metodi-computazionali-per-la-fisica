import math

#funzione per la somma dei primi n numeri naturali


def somma(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 += i
    
    return sum1

#funzione per la somma delle radici dei primi n numeri naturali


def somma_radici(n):
    sum2 = 0
    for i in range(1, n+1):
        sum2 += math.sqrt(i)
    
    return sum2

def somma_prodotto(n):
    sum3 = 0
    prod = 1
    for i in range(1, n+1):
        sum3 += i
        prod = prod * i

    return sum3, prod

def somma_alpha(n, a = 1):
    sum4 = 0
    for i in range(1, n+1):
        sum4 += i**a

    return sum4

    
