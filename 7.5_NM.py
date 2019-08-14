#Ejercicio 7.5. Dada una lista de números enteros, escribir una función que:
def es_primo(numero):
    """ devuelve si es primo o no  """
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
    return es_primo

def factorial(numero):
    """devuelve el factorial del numero """
    factorial = 1
    for i in range(numero):
        factorial *= numero
        numero -= 1
    return factorial

#print(factorial(4))

#a) Devuelva una lista con todos los que sean primos.

def son_primos(numeros:list):
    """ devuelve una lista con todos los numeros primos  """
    lista_primos = []
    for numero in numeros:
        if es_primo(numero):
            lista_primos.append(numero)
    return lista_primos

#print(son_primos([1,2,3,4,5,6,7,8,9,10,11,12]))

#b) Devuelva la sumatoria y el promedio de los valores.
def sum_prom(numeros:list):
    """ devuelve la suma y promedio  """
    suma = 0
    for numero in numeros:
        suma += numero
    promedio = suma // len(numeros)
    return [("suma", suma), ("promedio", promedio)]

#print(sum_prom([5,10,25,50]))

#c) Devuelva una lista con el factorial de cada uno de esos números.

def factoriales(numeros:list):
    """ devuelve una lista de factoriales  """
    factoriales = []
    for numero in numeros:
        fact = factorial(numero)
        factoriales.append(fact)
    return factoriales

print(factoriales([3,4,5,6]))