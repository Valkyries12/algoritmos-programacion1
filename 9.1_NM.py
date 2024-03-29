#Ejercicio 9.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
#Por ejemplo:
#>>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
#>>> print(tuplas_a_diccionario(l))
#{ 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]

def tuplas_a_diccionarios(lista:list):
    """ devuelve un diccionario donde las claves son los primeros elementos de las tuplas y los valores una lista con los segundo  """
    diccionario = {}
    for tupla in lista:
        if tupla[0] not in diccionario:
            diccionario[tupla[0]] = [tupla[1]]
        else:
            diccionario[tupla[0]].append(tupla[1])
    return diccionario

print(tuplas_a_diccionarios(l))