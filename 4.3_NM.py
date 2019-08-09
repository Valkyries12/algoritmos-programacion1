#Ejercicio 4.3. Escribir una función que reciba por parámetro una dimensión 𝑛, e imprima la matriz identidad correspondiente a esa dimensión.

def matriz_identidad(dimension:int):
    """ imprime la matriz identidad correspondiente a la dimension dada """
    aux = 0
    identidad = []
    for i in range(dimension):
        for k in range(dimension):
            identidad.append(0)
        identidad[i] = 1
        print(identidad)
        identidad = []

matriz_identidad(5)