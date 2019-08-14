#Ejercicio 7.12. Funciones que reciben funciones.
#a) Escribir una funcion llamada map, que reciba una función y una lista y devuelva la lista que resulta de aplicar la función recibida a cada uno de los elementos de la lista recibida.

def cuadrado(n):
    """ devuelve el cuadrado del numero  """
    return n * n

def map(funcion, lista:list):
    lista_prueba = []
    for i in range(len(lista)):
        resultado = funcion(lista[i])
        lista_prueba.append(resultado)
    return lista_prueba



#print(map(cuadrado, [2,4,5,6]))

#b) Escribir una función llamada filter, que reciba una función y una lista y devuelva una lista con los elementos de la lista recibida para los cuales la función recibida devuelve un valor verdadero.
def es_par(n):
    """ devuelve si el numero es par  """
    es_par = False
    if n % 2 == 0:
        es_par = True
    return es_par



def filter(funcion, lista:list):
    lista_prueba = []
    for elemento in lista:
        if funcion(elemento):
            lista_prueba.append(elemento)
    return lista_prueba

print(filter(es_par, [2,4,5,7,8,11,12]))

