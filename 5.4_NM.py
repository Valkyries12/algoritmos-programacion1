#Ejercicio 5.4. Utilizando la función randrange del módulo random, escribir un programa que obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número correcto.

import random

def aleatorio_secreto():
    """ genera un numero aleatorio y permite al usuario ingresar numeros hasta que sea igual al numero generado  """
    numero_aleatorio = random.randrange(1, 25)
    adivinar_numero = int(input("ingrese numero a adivinar: "))
    while adivinar_numero != numero_aleatorio:
        if adivinar_numero < numero_aleatorio:
            print("El numero a adivinar es mas alto")
        else:
            print("El numero a adivinar es mas bajo")
        adivinar_numero = int(input("ingrese numero a adivinar: "))
    print("Muy bien!")

aleatorio_secreto()