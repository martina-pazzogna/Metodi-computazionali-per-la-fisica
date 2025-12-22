import mycamera
import numpy as np
import ctypes
import matplotlib.pyplot as plt

#lettura immagine
inp = ctypes.create_string_buffer(1536 * 1024 * 2 )
lettura = mycamera.read_camera(inp)
 

#conversione opportuna dell'immagine
arr = np.frombuffer(lettura, dtype ='<u2')

righe = 1024
colonne = 1536

prov = arr.reshape((righe, colonne), order = 'C')

M = np.flipud(prov)

#visualizzazione dell'immagine
plt.imshow(M)
plt.show()


