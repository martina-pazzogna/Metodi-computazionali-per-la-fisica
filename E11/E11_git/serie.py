import numpy
import ctypes

#import della libreria
lib_serie = numpy.ctypeslib.load_library('libserie', '/home/martina/MCF/Metodi-computazionali-per-la-fisica/E11')

#definizione dei tipi di input e output
lib_serie.fibonacci.argtype = [ctypes.c_int]
lib_serie.fibonacci.restype = ctypes.c_double

#utilizzo della funzione Fibonacci 
def fibonacci(n):
    return lib_serie.fibonacci(int(n))

    
