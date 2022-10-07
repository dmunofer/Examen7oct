from vehiculo import *
class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} ruedas, {} km/h, {} cc".format( self.color, self.ruedas, self.velocidad, self.cilindrada )

    def getruedas(self):
        return self.ruedas

coche = Coche("azul", 4, 150, 1200)
coche2= Coche("negro", 5, 140, 1500)
print(coche)