def error1(a,b):
    if b==0:
        raise Exception('No puede haber un 0 en el denominador')
    return a/b