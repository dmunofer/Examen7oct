from alumnomain import Alumno

def calificacion(self):
    if self.nota>=5:
        print('Aprobado')
    else:
        print('Suspenso')

alumno1=Alumno('Diego',5)
alumno2=Alumno('Enrique',4)

calificacion(alumno1)
calificacion(alumno2)

