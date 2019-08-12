#Ejercicio 5.2. Escribir una función que reciba un número entero 𝑘 e imprima su descomposición en factores primos.

def descomposicion_primo(n):
    """ imprime la descomposicion de primos del numero pasado por parametro  """
    descomposicion = ""
    num = n
    primo = 2
    while num != 1:
        if num % primo == 0:
            descomposicion += f" {primo} "
            num = num / primo
        else:
            primo += 1
    print(descomposicion)

descomposicion_primo(24)