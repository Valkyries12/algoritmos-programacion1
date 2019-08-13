#Ejercicio 6.4. Escribir una función contar(c, s) que cuente cuántas veces aparece un carácter c dado en una cadena s.

def contar(caracter, cadena):
    """ retorna la cantidad de veces que esta la letra en la cadena dada """
    cantidad = 0
    for letra in cadena:
        if letra == caracter:
            cantidad += 1
    return cantidad

#Ejercicio 6.5. ¿Hay más letras “A” o más letras “E” en una cadena? Escribir un programa que lo decida.

def cual_hay_mas(cadena):
    """ imprime si hay mas letras A o E  """
    cantidad_A = 0
    cantidad_E = 0
    for letra in cadena:
        if letra == "a":
            cantidad_A += 1
        if letra == "e":
            cantidad_E += 1
    if cantidad_A < cantidad_E:
        print("Hay mas letraas E")
    else:
        print("Hay mas letras A")

#Ejercicio 6.6. Escribir un programa que cuente cúantas veces aparecen cada una de las vocales en una cadena. No importa si la vocal aparece en mayúscula o en minúscula.

def cantidad_vocales(cadena):
    cantidad_A = 0
    cantidad_E = 0
    cantidad_I = 0
    cantidad_O = 0
    cantidad_U = 0
    for letra in cadena:
        if letra == "a" or letra == "A":
            cantidad_A += 1
        if letra == "e" or letra == "E":
            cantidad_E += 1
        if letra == "i" or letra == "I":
            cantidad_I += 1
        if letra == "o" or letra == "O":
            cantidad_O += 1
        if letra == "u" or letra == "U":
            cantidad_U += 1
    print(f"A:{cantidad_A}, E:{cantidad_E}, I:{cantidad_I}, O:{cantidad_O}, U:{cantidad_U}")

#print(contar("e", "elefante"))
#cual_hay_mas("elefante")
cantidad_vocales("El elefante trompita tenia un orangutan")