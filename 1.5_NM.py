#Ejercicio 1.5. Implementar algoritmos que resuelvan los siguientes problemas:
#a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.

def suma(num1, num2):
    suma = num1 + num2
    return suma

print(suma(2,2))

def resta(num1, num2):
    resta = num1 - num2
    return resta

print(resta(4, 2))

def division(num1, num2):
    division = num1 // num2
    return division

print(division(4,2))

def multiplicacion(num1, num2):
    multi = num1 * num2
    return multi

print(multiplicacion(5,5))

#b) Dado un número entero 𝑛, imprimir su tabla de multiplicar.

def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{i} x {n} es {i * n}")

tabla_multiplicar(5)


