from vehiculo import *
from coche import *



def catalogar(lista, nruedas=-8):
    coincidenlasruedas=0
    if nruedas==-8:
        for elemento in lista:
            print(type(elemento).__name__, elemento)
    else:
        for elemento in lista:
            if elemento.getruedas()==nruedas:
                coincidenlasruedas+=1

            else:
                pass
        return "Se han encontrado {} vehículo(s) con {} ruedas".format(coincidenlasruedas,nruedas)

vehiculo1= Vehiculo("rojo",6)
coche = Coche("azul", 4, 150, 1200)
coche2= Coche("negro", 5, 140, 1500)
vehiculos=[coche, coche2, vehiculo1]