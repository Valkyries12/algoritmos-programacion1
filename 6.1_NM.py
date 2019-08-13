#Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
#a) Imprima los dos primeros caracteres.

def dos_primeros_char(cadena):
    """ imprime los dos primeros caracteres  """
    dos_char = cadena[:2]
    print(dos_char)

#dos_primeros_char("elefante")

#b) Imprima los tres últimos caracteres.

def tres_ultimos_char(cadena):
    """ imprime los 3 últimos caracteres  """
    tres_char = cadena[-3:]
    print(tres_char)

#tres_ultimos_char("elefante")

#c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'

def cada_dos_char(cadena):
    """ imprime la cadena cada dos caracteres  """
    cada_dos = cadena[::2]
    print(cada_dos)

#cada_dos_char("elefante")

#d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'

def inverso(cadena):
    """ imprime la cadena al revez  """
    revez = cadena[-1::-1]
    print(revez)

#inverso("Elefante")

#e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime 'reflejoojelfer'.

def espejo(cadena):
    """ imprime la cadena al deerecho y al reves  """
    espejo = cadena[-1::-1]
    entera = cadena + espejo
    print(entera)

espejo("elefante")