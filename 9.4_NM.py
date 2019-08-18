#Ejercicio 9.5.4. Escribir una función que reciba un texto y para cada caracter presente en el texto devuelva la cadena más larga en la que se encuentra ese caracter.
def cadena_mas_larga(cadena:str):
    """ devuelve por cada caracter la cadena mas larga en la que se encuentra dicho caracter  """
    diccionario = {}
    lista = cadena.split()
    for letra in cadena:
        if letra not in diccionario:
            diccionario[letra] = [0]
    for palabra in lista:
        for key in diccionario:
            if key in palabra:
                if len(palabra) > diccionario[key][0]:
                    diccionario[key] = [len(palabra), palabra]
    return diccionario

print(cadena_mas_larga("devuelve por cada caracter la cadena mas larga en la que se encuentra dicho caracter"))