#Ejercicio 5.10. Escribir una función que reciba un número natural e imprima todos los números primos que hay hasta ese número.

def es_primo(n):
    """ devuelve true si es primo o no """
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    return primo

def imprimir_primos(n):
    """ imprime todos los numeros primos que hay hasta el numero declarado  """
    if type(n) == str or n < 0:
        print("Error no ha ingresado un numero natural")
    else:
        x = 1
        while x < n:
            if es_primo(x):
                print(f"{x}", end=" - ")
            x += 1


imprimir_primos(126)