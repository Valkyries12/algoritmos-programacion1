#Ejercicio 2.6. Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el usuario, a cada uno le calcule el factorial e imprima el resultado junto con el número de orden correspondiente.
def factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= n
        n -= 1
    return factorial

def factoriales():
    cantidad = int(input("Cuantos valores vas a ingresar?: "))
    for i in range(cantidad):
        valor = int(input("Ingrese valor para hacer factorial: "))
        fact = factorial(valor)
        print(f"El factorial de {valor} es {fact}")

factoriales()