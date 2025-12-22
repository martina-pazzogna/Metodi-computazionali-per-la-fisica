import serie
import numpy as np

n = np.arange(20)

risultati = []
for i in range(len(n)):
    ris = serie.fibonacci(n[i])
    risultati.append(ris)

    
print("I risultati della funzione Fibonacci per i primi n numeri naturali sono: ", risultati)