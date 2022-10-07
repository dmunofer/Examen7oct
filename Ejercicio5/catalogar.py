from vehiculo import *
from coche import *

def catalogar(lista):
    for elemento in lista:
        print(type(elemento).__name__, elemento)

vehiculo1= Vehiculo("rojo",6)
vehiculos=[coche,coche2,vehiculo1]