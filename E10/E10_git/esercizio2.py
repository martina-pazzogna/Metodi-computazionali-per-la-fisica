import numpy as np
import matplotlib.pyplot as plt
import random_walk

N = 1000 #numero di passi
s = 0.01 #m- lunghezza del passo (1 cm)

for i in range(5):
    posizioni = random_walk.random_walk(s, N)
    plt.plot(posizioni[0], posizioni[1], label = 'Particella ' + str(i+1))


plt.legend(loc = 'best')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.xlim(-0.4,0.4)
plt.ylim(-0.4,0.4)
plt.title('Random walk')
plt.grid(True)
plt.show()

def distanza(x,y):
    
    """
    Parametri: x e y sono le coordinate della posizione della particella per ciascun passo

    Restituisce la distanza dall'origine

    """

    return np.sqrt(x**2 + y**2)

fig, ax = plt.subplots(2,1, figsize=(5,8))
for i in range(5):
    posizioni = random_walk.random_walk(s, N)
    distanze = []
    for k in range(len(posizioni[0])):
        d = distanza(posizioni[0][k], posizioni[1][k])
        distanze.append(d)

    ax[0].plot(posizioni[0], posizioni[1], label = 'Particella ' + str(i+1))
    ax[1].plot(np.arange(N+1), np.array(distanze), label='Particella ' + str(i+1))

ax[0].set_xlabel('x [m]')
ax[0].set_ylabel('y [m]')
ax[0].set_title('Random walk')
ax[0].legend(loc = 'best')

ax[1].set_xlabel('N')
ax[1].set_ylabel('Distanza [m]')
ax[1].set_title('Distanza dall\' origine in funzione dei passi')
ax[1].legend(loc = 'best')

plt.show()

