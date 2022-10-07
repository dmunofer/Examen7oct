from vehiculo import *
from coche import *
import catalogar

coche = Coche("azul", 150, 4, 1200)
coche2= Coche("negro", 180, 5, 1500)
vehiculo1= Vehiculo("rojo",6)

vehiculos=[coche,coche2,vehiculo1]
catalogar.catalogar(vehiculos)


