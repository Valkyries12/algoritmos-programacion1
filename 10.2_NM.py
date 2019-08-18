#Ejercicio 10.2. Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo (sea de texto o binario) a otro, de modo que quede exactamente igual.
#Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.

def cp(archivo_a_copiar, copia_archivo):
    """ copia el contenido de un archivo hacia otro  """
    datos = ""
    with open(archivo_a_copiar) as archivo:
        datos = archivo.read(2400)
    with open(copia_archivo, "w") as archivo:
        archivo.write(datos)
    print("datos copiados satisfactoriamente")

cp("lorem.txt", "copia_lorem.txt")