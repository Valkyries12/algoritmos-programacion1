#Ejercicio 2.4. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

def todos_los_pares(n1, n2):
    for i in range(n1, n2):
        if i % 2 == 0:
            print(i, end=" - ")

todos_los_pares(1,11)