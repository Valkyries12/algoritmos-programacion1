#Ejercicio 6.6. Escribir funciones que dada una cadena de caracteres:
#a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o 'logaritmos' debe devolver 'lgrtms'.

def devolver_consonantes(cadena):
    """ devuelve solo las consonantes """
    vocales = ["a", "e", "i", "o", "u"]
    palabra = ""
    for letra in cadena:
        if letra not in vocales:
            palabra += letra
    return palabra

#print(devolver_consonantes("algoritmos"))

#b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe devolver 'i ooae'.


def devolver_vocales(cadena):
    """ devuelve solo las vocales  """
    vocales = ["a", "e", "i", "o", "u", " "]
    palabra = ""
    for letra in cadena:
        if letra in vocales:
            palabra += letra
    return palabra

#print(devolver_vocales("sin consonantes"))

#c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe devolver 'vistaerou'.

def reemplazar_por_siguiente_vocal(cadena):
    """ Reemplaza cada vocal con la siguiente vocal  """
    vocales = ["a", "e", "i", "o", "u"]
    palabra = ""
    for i in range(len(cadena)):
        if cadena[i] in vocales:
            if cadena[i] == "u":
                palabra += "a"
            for k in range(len(vocales)-1):
                if cadena[i] == vocales[k]:
                    palabra += vocales[k+1]
        else:
            palabra += cadena[i]
    return palabra

#print(reemplazar_por_siguiente_vocal("vestuario"))

#d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def es_palindromo(cadena):
    """ Devuelve si es palindromo o no la cadena dada  """
    completa = ""
    es_palindromo = False
    for letra in cadena:
        if letra == " ":
            continue
        else:
            completa += letra
    revez = completa[-1::-1]
    if completa == revez:
        es_palindromo = True
    return es_palindromo

print(es_palindromo("anita lava la tina"))


