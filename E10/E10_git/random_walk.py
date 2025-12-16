import numpy as np
import matplotlib.pyplot as plt

def random_walk(s, N):
    """
    parametri: s = lunghezza (costante) del passo
               N = numero di passi

    Restituisce un array 2D con le coordinate x e y della particella dopo ciascun passo

    """
    angoli = np.random.uniform(low = 0, high = (2 * np.pi), size = N)
    x_pos = [0]
    y_pos = [0]

    for i in range(N):
        delta_x = s * np.cos(angoli[i])
        delta_y = s * np.sin(angoli[i])

        x = x_pos[i] + delta_x
        y = y_pos[i] + delta_y

        x_pos.append(x)
        y_pos.append(y)

    posizioni = np.array([np.array(x_pos), np.array(y_pos)])

    return posizioni


