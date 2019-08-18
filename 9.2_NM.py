#Ejercicio 9.2. Diccionarios usados para contar.
import random
#a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.

def cuenta_palabras(cadena:str):
    """ devuelve un diccionario con la cantidad de apariciones de cada palabra en la cadena  """
    diccionario = {}
    lista = cadena.split()
    for palabra in lista:
        if palabra not in diccionario:
            diccionario[palabra] = 0
    for palabra in lista:
        if palabra in diccionario:
            diccionario[palabra] += 1
    return diccionario

#print(cuenta_palabras("que lindo dia que hace hoy"))


#b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, y los devuelva en un diccionario.

def cuenta_caracteres(cadena:str):
    """ devuelve un diccionario con la cantidad de apariciones de cada caracter en la cadena """
    diccionario = {}
    for letra in cadena:
        if letra not in diccionario:
            diccionario[letra] = 0
    for letra in cadena:
        if letra in diccionario:
            diccionario[letra] += 1
    return diccionario

#print(cuenta_caracteres("elefanteelefante"))


#c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.
#Nota: utilizar el módulo random para obtener tiradas aleatorias.

def cuenta_dados(n:int):
    """ devuelve la cantidad de veces que se observa cada valor de la suma de los dados  """
    diccionario = {}
    for i in range(n):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        if suma not in diccionario:
            diccionario[suma] = 0
        if suma in diccionario:
            diccionario[suma] += 1
    return diccionario

print(cuenta_dados(5))