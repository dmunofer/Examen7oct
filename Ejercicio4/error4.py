def error4(a,b):
    if type(a)!= type(b):
        raise Exception('No se pueden sumar variables de distinto tipo')
    else:
        return a+b