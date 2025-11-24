import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#variabili utilizzate
l1 = 0.5 #m
theta_01 = np.pi / 4 #rad
w0 = 0
r01 = (theta_01, w0)
def equazione_differenziale(r,t,g,l):

    """
    r : vettore di componenti (theta, w)
    t : tempo

    -------

    restituisce il sistema di equazioni:
    1) d(theta)/dt = w
    2) dw/dt = -g/l sin(theta)

    """

    dxdt = r[1]
    dydt = -g/l * np.sin(r[0])
    drdt = [dxdt, dydt]

    return drdt

#Grafico soluzione -caso 1
time = np.linspace(0,10, 1000)
sol1 = integrate.odeint(equazione_differenziale, r01, time, args = (9.81, l1))

plt.plot(time, sol1[:, 1])
plt.xlabel('time [s]')
plt.ylabel('theta(t) [rad]')
plt.grid(True)
plt.title('Risultato dell\' equazione differenziale')
plt.show()


#caso 2
l2 = 1 #m
theta_02 = np.pi/4 #rad
r02 = (theta_02, w0)

#Grafico soluzione -caso 2
sol2 = integrate.odeint(equazione_differenziale, r02, time, args = (9.81, l2))

plt.plot(time, sol2[:, 1])
plt.xlabel('time [s]')
plt.ylabel('theta(t) [rad]')
plt.grid(True)
plt.title('Risultato dell\' equazione differenziale')
plt.show()

#caso 3
theta_03 = np.pi/6 #rad
r03 = (theta_03, w0)

sol3 = integrate.odeint(equazione_differenziale, r03, time, args = (9.81, l1))

#Grafico soluzione -caso 3
plt.plot(time, sol3[:, 1])
plt.xlabel('time [s]')
plt.ylabel('theta(t) [rad]')
plt.grid(True)
plt.title('Risultato dell\' equazione differenziale')
plt.show()

#grafico confronto caso 1 e 3
plt.plot(time, sol3[:, 1], label = 'theta_0 = 30°')
plt.plot(time, sol1[:, 1], label = 'theta_0 = 45°')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('theta(t) [rad]')
plt.grid(True)
plt.title('RConfronto dei due andamenti (con stessa lunghezza)')
plt.show()