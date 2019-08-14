#Ejercicio 7.1. Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no.

def esta_ordenado(tupla):
    """ devuelve si la tupla esta ordenada de menor a mayor  """
    esta_ordenada = False
    tupla_ordenada = sorted(tupla)
    tupla_ordenada = tuple(tupla_ordenada)
    if tupla_ordenada == tupla:
        esta_ordenada = True
    return esta_ordenada

print(esta_ordenado((6, 2, 3)))