def error3(dict,clave):
    if clave not in dict:
        raise Exception('La clave no se encuentra en el diccionario')
    else:
        return dict[clave]

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
error3(paises, "alemania")