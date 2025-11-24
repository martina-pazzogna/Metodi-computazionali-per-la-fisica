import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#variabili
x0 = 0 #m
y0 = 0 #m
vx0 = 3 #m/s
vy0 = 5 #m/s

r0 = (x0, y0, vx0, vy0)

#equazione differenziale
def equazione_differenziale(r,t, wx, wy):

    """
    r: vettore di componenti (x,y, dx/dt, ,dy/dt)
    t: tempo

    -----
    restituisce il sistema :
    1) vx = dx/dt (z)
    2) vy = dy/dt (k)
    3) dvx/dt = -wx^2 x
    4) dvy/dt = -wy^2 y

    """

    dxdt = r[2]
    dydt = r[3]
    dzdt = -wx**2 * r[0]
    dkdt = -wy **2 * r[1]

    drdt = [dxdt, dydt, dzdt, dkdt]
    return drdt

time = np.linspace(0,10, 1000)
soluzione = integrate.odeint(equazione_differenziale, r0, time, args = (2, 5) )

plt.plot(time, soluzione[:, 0], label = 'vx(t)')
plt.plot(time, soluzione[:,2], label = 'x(t)')
plt.xlabel('time[s]')
plt.ylabel('spazio e velocità')
plt.grid(True)
plt.legend()
plt.show()


plt.plot(time, soluzione[:, 1], label = 'vy(t)')
plt.plot(time, soluzione[:,3], label = 'y(t)')
plt.xlabel('time[s]')
plt.ylabel('spazio e velocità')
plt.grid(True)
plt.legend()
plt.show()

#grafico traiettoria 
plt.plot(soluzione[:, 2], soluzione[:, 3])
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.grid(True)
plt.title('Traiettoria')
plt.show()