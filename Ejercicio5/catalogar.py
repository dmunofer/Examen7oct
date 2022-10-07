from vehiculo import Vehiculo
from coche import *

def catalogar(lista, nruedas=-8):
    coincidenlasruedas=0
    if nruedas ==-8:
        for elemento in lista:
            print(type(elemento).__name__, elemento)

    elif Vehiculo.ruedas==nruedas:
            cont+=1
    else:
        pass

    return "Se han encontrado {} vehículo(s) con {} ruedas".format(coincidenlasruedas,nruedas)

vehiculo1= Vehiculo("rojo",6)
vehiculos=[coche,coche2,vehiculo1]