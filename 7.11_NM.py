#Ejercicio 7.11. Plegado de un texto. Escribir una función que reciba un texto y una longitud y devuelva una lista de cadenas de como máximo esa longitud. Las líneas deben ser cortadas correctamente en los espacios (sin cortar las palabras).

def plegado_texto(texto:str, longitud:int):
    """ devuelve una lista de cadenas de como maximo la longitud dada """
    lista = texto.split()
    for i in range(len(lista)):
        for k in range(len(lista[i])):
            if len(lista[i]) > longitud:
                palabra_quitada = lista.pop(i)
                palabra_quitada = palabra_quitada[:longitud]
                lista.insert(i, palabra_quitada)
    return lista

print(plegado_texto("devuelve una lista de cadenas de como maximo la longitud dada", 5))