#Ejercicio 5.6. Potencias de dos.
#a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
#b) Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función es_potencia_de_dos, descripta en el punto anterior.

def es_potencia_de_dos(n):
    """ Me devuelve True o False si el numero pasado por parametro es potencia o no """
    if n < 0:
        print("Error no es numero natural")
        return
    potencia = 1
    es_potencia = None
    while 2 ** potencia <= n:
        if 2 ** potencia == n:
            es_potencia = True
        else:
            es_potencia = False
        potencia += 1
    return es_potencia

def suma_rangos_potencias(a, b):
    """ devuelve la suma de las potencias de 2 en el rango indicado  """
    if es_potencia_de_dos(a)  or es_potencia_de_dos(b):
        print("Error algunos de los numeros indicados no es natural")
        return
    suma = 0
    if a < b:
        mayor = b
        menor = a
    else:
        mayor = a
        menor = b
    for i in range(menor, mayor):
        if es_potencia_de_dos(i):
            suma += i
    return suma

#print(es_potencia_de_dos(7))
print(suma_rangos_potencias(1, 10))