#Ejercicio 5.9. Escribir una función que reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.
#a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
#b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor que el segundo.

def rango_multiplo(a, b):
    """ devuelve la cantidad de multiplos que hay entre los rangos  """
    cantidad_multiplos = 0
    multiplo = 1
    for i in range(a, b):
        if a * multiplo <= b:
            multiplo += 1
    return multiplo

def rango_multiplo_while(a, b):
    """ devuelve la cantidad de multiplos que hay entre los rangos  """
    cantidad_multiplos = 0
    multiplo = 1
    while a * multiplo < b:
        multiplo += 1
    return multiplo

#print(rango_multiplo(5, 25))
print(rango_multiplo_while(5, 25))