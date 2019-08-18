#Ejercicio 10.1. Escribir un programa, llamado head que reciba un archivo y un número N e imprima las primeras N líneas del archivo.

def head(archivo, n:int):
    """ imprime las primeras n lineas del archivo  """
    with open(archivo) as f:
        i = 1
        while i <= n:
            oracion = f.readline()
            print(oracion)
            i += 1

head("lorem.txt", 2)