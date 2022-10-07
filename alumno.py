class Alumno():

    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        print(self.nombre, self.nota)

    def calificacion(self):
        if self.nota>=5:
            print('Aprobado')
        else:
            print('Suspenso')

alumno1=Alumno('Diego',5)
alumno2=Alumno('Enrique',4)

Alumno.calificacion(alumno1)
Alumno.calificacion(alumno2)

