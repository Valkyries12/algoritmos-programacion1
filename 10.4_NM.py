#Ejercicio 10.4. Escribir un programa, llamado wc.py que reciba un archivo, lo procese e imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.

def wc(archivo):
    """ imprime las lineas, palabras y caracteres que contiene el archivo  """
    lineas = 0
    palabras = 0
    caracteres = 0
    with open(archivo) as f:
        datos = f.readlines()
        for line in datos:
            lineas += 1
            lista_linea = line.split()
            for palabra in lista_linea:
                palabras += 1
                caracteres += len(palabra)
    print(f"lineas: {lineas}")
    print(f"palabras: {palabras}")
    print(f"caracteres: {caracteres}")

wc("lorem.txt")