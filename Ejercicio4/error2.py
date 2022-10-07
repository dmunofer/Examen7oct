def error2(lista, posicion):
    longitud = len(lista)
    if posicion+1>longitud:
        raise Exception('El índice introducido está fuera del rango de la lista')
    else:
        return lista[posicion]

lista = [4, 7, 30, 23, 5]
error2(lista,10)