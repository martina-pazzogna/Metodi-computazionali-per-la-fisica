import numpy as np
import matplotlib.pyplot as plt
import classi_es3

n = 30 #numero di particelle che attraversano il rivelatore

rivelatore = classi_es3.rivelatore(0.01, 5, 10**(-6), 10**(-7), 10**(-12), 10**4 )
gen = []
riv = []
der = []

for i in range(n):
    evento = classi_es3.evento(rivelatore)

    coppie_generate, numero_rivelati, tempi_deriva, posizioni_iniziali = evento.caratteristiche_evento()
    gen.append(coppie_generate)
    riv.append(numero_rivelati)
    der.append(tempi_deriva)

generati = np.array(gen) #array che contiene il numero di coppie generate per ciascun evento
rivelati = np.array(riv) #array che contiene il numero di coppie rivelate per ciascun evento
deriva = np.array(der, dtype = object) #array che contiene l'array dei tempi di deriva per ciascun evento

tempi_deriva_complessivi = np.hstack(deriva) #tempi di deriva di tutti gli elettroni di tutti gli eventi


minim = []
for i in range(n):
    if (len(deriva[i]) == 0):
        minimo = 0
        minim.append(minimo)
    else:
        minimo = np.min(deriva[i])
        minim.append(minimo)

deriva_minimi = np.array(minim) #array dei tempi di deriva minimi per ciascun evento

med = []
for i in range(n):
    if (len(deriva[i]) == 0):
        medio = 0
        med.append(medio)
    else:
        medio = np.mean(deriva[i])
        med.append(medio)

deriva_medi = np.array(med) #array dei tempi di deriva medi per ciascun evento

#istogrammi
plt.hist(rivelati, bins = 7, color = 'purple')
plt.xlabel('Numero di cariche rivelate')
plt.ylabel('Occorrenza')
plt.title('Distribuzione del numero di coppie rivelate')
plt.show()



plt.hist(tempi_deriva_complessivi, bins = int(np.sqrt(len(tempi_deriva_complessivi))), color = 'orange')
plt.xlabel('Tempi di deriva [s]' )
plt.ylabel('Occorrenza')
plt.title('Distribuzione dei tempi di deriva')
plt.show()


plt.hist(deriva_minimi, bins = int(len(deriva_minimi)), color = 'green')
plt.xlabel('Tempi di deriva minimi [s]')
plt.ylabel('Occorrenza')
plt.title('Distribuzione dei tempi di deriva minimi')
plt.show()

plt.hist(deriva_medi, bins = int(len(deriva_medi)), color = 'green')
plt.xlabel('Tempi di deriva medi [s]')
plt.ylabel('Occorrenza')
plt.title('Distribuzione dei tempi di deriva medi')
plt.show()

#calcolo delle efficienze di rivelazione di un elettrone e di una particella
efficienza_elettrone= (np.sum(rivelati)/np.sum(generati))*100
print('L\'efficienza con la quale viene rivelato un elettrone generato dal passaggio di una particella carica è del ', efficienza_elettrone, '%')

particella_rivelata = 0
for i in range(n):
    if (rivelati[i] != 0):
        particella_rivelata += 1

efficienza_particella = (particella_rivelata/n)*100
print('L\'efficienza con la quale viene rivelata una particella carica è del ', efficienza_particella, '%')

