#Ejercicio 7.9. Escribir una función que reciba como parámetro una cadena de palabras separadas por espacios y devuelva, como resultado, cuántas palabras de más de cinco letras tiene la cadena dada.

def cantidad_mas_de_cinco(cadena):
    """ devuelve cuantas palabras tienen mas de 5 letras  """
    lista = cadena.split()
    cantidad = 0
    for elemento in lista:
        if len(elemento) > 5:
            cantidad += 1
    return cantidad

print(cantidad_mas_de_cinco("Habia una vez un barco chiquitito que nadaba sin atencion"))