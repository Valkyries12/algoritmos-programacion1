#Ejercicio 10.5. Escribir un programa, llamado grep.py que reciba una expresión y un archivo e imprima las líneas del archivo que contienen la expresión recibida.

def grep(archivo, expresion):
    """ imprime la linea que contiene la expresion recibida """
    with open(archivo) as f:
        datos = f.readlines()
        for linea in datos:
            lista = linea.split()
            if expresion in lista:
                print(linea)

grep("lorem.txt", "5")