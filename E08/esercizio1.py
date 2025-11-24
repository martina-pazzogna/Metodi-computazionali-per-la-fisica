import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--caso1", help = "Mostra i risultati del caso 1", action = "store_true")
parser.add_argument("--caso2", help ="Mostra i risultati del caso 2", action = "store_true")
parser.add_argument("--caso3", help ="Mostra i risultati del caso 3", action = "store_true")
args= parser.parse_args()

#variabili
m = 0.2 #kg
k = 2 #N/mC
C = 0.5 #Ns/m
gamma = C/ (2 * m)
w0 = np.sqrt(k / m)

#condizioni iniziali
x0 = 0
v0 = 0
r0 = [x0, v0]

#funzione che rappresenta l'equazione differenziale
def equazione_diff(r, t, w0, C, m, f, wf):
    dxdt = r[1]
    dydt = -w0**2 * r[0] - C/m * r[1] + f(t, wf)/m
    drdt = [dxdt, dydt]
    """
    r= vettore con variabili (x, dx/dt) 
    f(t) = funzione da passare come variabile dipendente dal tempo
    
    -------
    restituisce il sistema di equazioni:
    1) y = dx/dt
    2) dy/dt = -w0^2 x - C/m y + f(t)/m^2

    """
    return drdt

#funzione che descrive la forza esterna (caso 1)
def f1(t, wf):

    """
    variabile: t
    parametro: pulsazione

    """
    return 2 * np.sin(wf * t)

#soluzione equazione differenziale (caso 1)
time = np.linspace(0,10, 1000)
sol1 = integrate.odeint(equazione_diff, r0, time, args = (w0, C, m, f1, 2))

#grafici soluzioni caso 1
plt.plot(time, f1(time, 2))
plt.xlabel('time [s]')
plt.ylabel('force [N]')
plt.title('Andamento della forza esterna')
plt.grid(True)
if args.caso1:
    plt.show()

plt.plot(time, sol1, label = ('v(t)', 'x(t)'))
plt.xlabel('time[s]')
plt.ylabel('Velocità e spazio')
plt.title("Risultati dell'equazione differenziale")
plt.grid(True)
plt.legend()
if args.caso1:
    plt.show()

#calcolo dell'ampiezza di oscillazione massima al variare di wf
int_w = np.linspace(0,10, 1000)

massimi = []

for i in range(len(int_w)):
    sol = integrate.odeint(equazione_diff, r0, time, args = (w0, C, m, f1, int_w[i]))
    x_t = sol[:, 1]
    max_ = np.max(x_t)

    massimi.append(max_)

#grafico che mostra l'andamento dell'ampiezza di oscillazione al variare di wf
y = np.array(massimi)

plt.plot(int_w, y)
plt.xlabel('Pulsazione forza esterna [s^-1]')
plt.ylabel('Ampiezza massima di oscillazione [m]')
plt.title('Grafico che mostra l\'andamento dell\' ampiezza di oscillazione massima al variare di wf')
plt.grid('True')
if args.caso1:
    plt.show()


#funzione che descrive la forza esterna (caso 2)
def f2(t, wf):

    """
    variabile: t
    parametro: pulsazione

    """
    return 2 * np.sin(wf * t) + np.sin(2 * wf * t)

#soluzione equazione differenziale (caso 2)
sol2 = integrate.odeint(equazione_diff, r0, time, args = (w0, C, m, f2, 2))

#grafici soluzioni caso 2
plt.plot(time, f2(time, 2))
plt.xlabel('time [s]')
plt.ylabel('force [N]')
plt.title('Andamento della forza esterna')
plt.grid(True)
if args.caso2:
    plt.show()

plt.plot(time, sol2, label = ('v(t)', 'x(t)'))
plt.xlabel('time[s]')
plt.ylabel('Velocità e spazio')
plt.title("Risultati dell'equazione differenziale")
plt.grid(True)
plt.legend()
if args.caso2:
    plt.show()

#calcolo dell'ampiezza di oscillazione massima al variare di wf
massimi2 = []

for i in range(len(int_w)):
    sol = integrate.odeint(equazione_diff, r0, time, args = (w0, C, m, f2, int_w[i]))
    x_t = sol[:, 1]
    max_ = np.max(x_t)

    massimi2.append(max_)

#grafico che mostra l'andamento dell'ampiezza di oscillazione al variare di wf
y2 = np.array(massimi2)

plt.plot(int_w, y2)
plt.xlabel('Pulsazione forza esterna [s^-1]')
plt.ylabel('Ampiezza massima di oscillazione [m]')
plt.title('Grafico che mostra l\'andamento dell\' ampiezza di oscillazione massima al variare di wf')
plt.grid('True')
if args.caso2:
    plt.show()


#funzione che descrive la forza esterna (caso 3)
def f3(t, wf):

    """
    variabile: t
    parametro: pulsazione

    """
    return 2 * (t/0.2)**2 * np.exp(-t/0.2)

#soluzione equazione differenziale (caso 3)
sol3 = integrate.odeint(equazione_diff, r0, time, args = (w0, C, m, f3, 2))

#grafici soluzioni caso 3
plt.plot(time, f3(time, 2))
plt.xlabel('time [s]')
plt.ylabel('force [N]')
plt.title('Andamento della forza esterna')
plt.grid(True)
if args.caso3:
    plt.show()

plt.plot(time, sol3, label = ('v(t)', 'x(t)'))
plt.xlabel('time[s]')
plt.ylabel('Velocità e spazio')
plt.title("Risultati dell'equazione differenziale")
plt.grid(True)
plt.legend()
if args.caso3:
    plt.show()

#calcolo dell'ampiezza di oscillazione massima al variare di wf

massimi3 = []

for i in range(len(int_w)):
    sol = integrate.odeint(equazione_diff, r0, time, args = (w0, C, m, f1, int_w[i]))
    x_t = sol[:, 1]
    max_ = np.max(x_t)

    massimi3.append(max_)

#grafico che mostra l'andamento dell'ampiezza di oscillazione al variare di wf
y3 = np.array(massimi3)

plt.plot(int_w, y3)
plt.xlabel('Pulsazione forza esterna [s^-1]')
plt.ylabel('Ampiezza massima di oscillazione [m]')
plt.title('Grafico che mostra l\'andamento dell\' ampiezza di oscillazione massima al variare di wf')
plt.grid('True')
if args.caso3:
    plt.show()
