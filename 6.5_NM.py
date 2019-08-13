#Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
#a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe devolver 'USB'.

def recorte_de_primera_letra_mayus(cadena):
    """ devuelve la primera letra de cada palabra en mayus  """
    palabra_final = ""
    primera_letra = ""
    for i in range(len(cadena)):
        primera_letra += cadena[i]
        if cadena[i] == " ":
            palabra_final += primera_letra[0]
            primera_letra = ""
    palabra_final += primera_letra[0]
    return palabra_final

#print(recorte_de_primera_letra_mayus("Universal Serial Bus"))

#b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe 'república argentina' debe devolver 'República Argentina'.
def primera_letra_mayus(cadena):
    """ devuelve la primera letra de cada palabra en mayus  """
    palabra_final = ""
    aux = ""
    for i in range(len(cadena)):
        aux += cadena[i]
        if cadena[i] == " ":
            palabra_final += aux.capitalize()
            aux = ""
    palabra_final += aux.capitalize()
    return palabra_final

#print(primera_letra_mayus("republica argentina"))




