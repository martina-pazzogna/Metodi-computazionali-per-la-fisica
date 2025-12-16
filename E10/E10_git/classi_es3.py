import numpy as np
import matplotlib.pyplot as plt

#classe che descrive la geometria della camera
class rivelatore:
    def __init__(self, spessore, numero, su, sf, tc, nr):
        """
        costruisce la geometria del rivelatore, 
        definendone spessore e numero medio di coppie generate e alcuni passi

        """
        self.s = spessore
        self.coppie_medie = numero
        self.su = su #passo uniforme
        self.sf = sf #passo generato dal campo elettrico
        self.tc = tc #tempo medio tra due urti dell'elettrone durante la diffusione
        self.nr = nr #adottato per descrivere la probabilità di assorbimento

    def passaggio_particella(self):
        """
        implementa la simulazione del passaggio di una
        particella ionizzante

        """
        self.coppie_gen = np.random.poisson(lam = self.coppie_medie)  
        
        pos = []
        for i in range(self.coppie_gen):
            y = np.random.uniform(low = 0, high = self.s)
            pos.append(y)

        self.posizioni_coppie = np.array(pos)
        
        return self.coppie_gen, self.posizioni_coppie

    def diffusione_elettroni(self):
        """
        simula la diffusione degli elettroni

        """

        n= len(self.posizioni_coppie)
        self.n_passi = np.zeros(n) #tiene conto del numero di passi di ciascun elettrone
        self.elettroni_rivelati = 0 #tiene il conto del numero di elettroni rivelati
        self.p_assorbimento = 1/self.nr #probabilità di assorbimento

        posizioni_var = self.posizioni_coppie.copy()
        for i in range(n):
            while ((self.s - posizioni_var[i] > 0.0001)): #condizione per cui l'elettrone si può dire rivelato
                x = np.random.random()
                if (x > self.p_assorbimento): #l'elettrone non è stato assorbito e, dunque, può proseguire il cammino
                    angolo = np.random.uniform(low = 0, high = 2*np.pi)
                    delta_y = self.sf + self.su * np.sin(angolo)
                    posizioni_var[i] += delta_y
                    self.n_passi[i] += 1

                else:
                    self.n_passi[i] = 0
                    break

            if (self.s - posizioni_var[i] < 0.0001):
                self.elettroni_rivelati += 1

        return self.elettroni_rivelati       
    
    def tempo_deriva(self):

        """
        calcola il tempo di deriva di ciascun elettrone sulla base del numero di passi compiuti 

        """
        deriva = []
        mask = self.n_passi > 0

        for i in range(len(self.n_passi[mask])):
            t = self.tc * self.n_passi[mask][i]
            deriva.append(t)

        self.tempi_deriva = np.array(deriva)

        return self.tempi_deriva
        

class evento:
    def __init__(self, rivelatore):

        """

        indico che rivelatore è stato adottato per compiere la misurazione

        """
        self.tipo_rivelatore = rivelatore
    
    def caratteristiche_evento(self):

        """
        Permette di ottenere contemporaneamente tutte le informazioni sull'evento

        """

        self.coppie_generate, self.posizioni =self.tipo_rivelatore.passaggio_particella()
        self.rivelati = self.tipo_rivelatore.diffusione_elettroni()
        self.tempi_deriva = self.tipo_rivelatore.tempo_deriva()

        return self.coppie_generate, self.rivelati, self.tempi_deriva, self.posizioni

        
    
            
            






      
    