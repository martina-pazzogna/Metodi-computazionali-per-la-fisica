import numpy
import ctypes

#import della libreria
lib_camera = numpy.ctypeslib.load_library('libmycamera', '/home/martina/MCF/Metodi-computazionali-per-la-fisica/E11')

#definizione dei tipi di input e output 
lib_camera.read_camera.argtype = [ctypes.c_char_p]
lib_camera.read_camera.restype = ctypes.c_int

#funzione read_camera

def read_camera(inp):

    out = lib_camera.read_camera(inp)

    return inp




