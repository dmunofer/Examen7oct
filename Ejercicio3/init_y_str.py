class Producto():

    def __init__(self,codigo, nombre, precio, tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        print(self.codigo, self.nombre, self.precio, self.tipo)

    def __str__(self):
        return "Código: {}, Nombre: {} , Precio: {} , Tipo: {} ".format(self.codigo, self.nombre, self.precio, self.tipo)
