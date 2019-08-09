#Ejercicio 1.4. Implementar un algoritmo que, dado un número entero 𝑛, permita calcular su factorial.

def factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= n
        n -= 1
    return factorial

print(factorial(4))