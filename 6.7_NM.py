#Ejercicio 6.7. Escribir funciones que dadas dos cadenas de caracteres:
#a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena' es una subcadena de 'subcadena'.

def es_subcadena(cadena, subcadena):
    """ devuelve si la segunda cadena es una subcadena de la primera  """
    es_subcadena = False
    if subcadena in cadena:
        es_subcadena = True
    return es_subcadena

#print(es_subcadena("subcadena", "cadena"))

#b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome' debe devolver 'gnome'.

def devolver_anterior_orden_alfabetico(cadena1, cadena2):
    """ Devuelva la que sea anterior en orden alfábetico  """
    if cadena1 < cadena2:
        return cadena1
    else:
        return cadena2

print(devolver_anterior_orden_alfabetico("kde", "gnome"))
