import pandas as pd
import matplotlib.pyplot as plt

pianeti = pd.read_csv('ExoplanetsPars_2025.csv', comment = '#')
print(pianeti.columns)

#grafico della massa in funzione del periodo orbitale

plt.scatter(pianeti['pl_orbper'], pianeti['pl_bmassj'], color='blue')
plt.xlabel('Periodo orbitale [days]')
plt.ylabel('Massa del pianeta [Jupiter Mass]')
plt.title('Massa del pianeta in funzione del periodo orbitale')
plt.xscale('log')
plt.yscale('log')
plt.show()

#grafico
y_array = pianeti['pl_orbsmax']**2/pianeti['st_mass']
plt.scatter(pianeti['pl_orbper'], y_array, color='blue')

plt.ylabel('$R^2_{max}/m$ [au/Solar Mass]')
plt.title('$R^2_{max}/m$ in funzione della massa')
plt.xscale('log')
plt.yscale('log')
plt.show()

#grafico
transit = pianeti.loc[pianeti['discoverymethod'] == 'Transit']
radial = pianeti.loc[pianeti['discoverymethod'] == 'Radial Velocity']

plt.scatter(transit['pl_orbper'], transit['pl_bmassj'], color = 'blue', alpha= 0.7, label= 'Metodo di scoperta = Transit')
plt.scatter(radial['pl_orbper'], radial['pl_bmassj'], color = 'orange', alpha= 0.3, label = 'Metodo di scoperta = Radial Velocity')
plt.xlabel('Periodo [Days]')
plt.ylabel('Massa del pianeta [Jupiter Mass]')
plt.title('Massa in funzione del periodo orbitale')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

#creazione dell'istogramma
n, bins, p = plt.hist(transit['pl_bmassj'], bins = 100, range= (0,100), color = 'blue', alpha = 0.7, label='Metodo di scoperta= Transit')
n1, bins1, p1 = plt.hist(radial['pl_bmassj'], bins = 100, range = (0,100), color = 'orange', alpha = 0.3, label='Metodo di scoperta= Transit Velocity')
plt.ylabel('Numero di pianeti')
plt.legend()
plt.xlabel('Massa [Jupiter Mass]')
plt.title('Istogramma della massa dei pianeti')
plt.show()

#creazione istrogramma
n, bins, p = plt.hist(transit['pl_bmassj'], bins = 1000, range= (10**(-4),100), color = 'blue', alpha = 0.7, label='Metodo di scoperta= Transit')
n1, bins1, p1 = plt.hist(radial['pl_bmassj'], bins = 1000, range = (10**(-4),100), color = 'orange', alpha = 0.3, label='Metodo di scoperta= Transit Velocity')
plt.ylabel('Numero di pianeti')
plt.legend()
plt.xlabel('Massa [Jupiter Mass]')
plt.xscale('log')
plt.title('Istogramma del logaritmo in base 10 della massa dei pianeti')
plt.show()
