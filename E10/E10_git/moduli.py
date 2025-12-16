import numpy as np
import matplotlib.pyplot as plt

#classe che descrive la geometria della camera
class geometria_rivelatore:
    def __init__(self):
        self.s = 0
        self.coppie = 0

    def costruzione(self, spessore, numero):
        self.s = spessore
        self.coppie = numero

#implementazione della simulazione del passaggio di una particella carica
      
    