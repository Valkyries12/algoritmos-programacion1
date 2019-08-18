#Ejercicio 10.6. Escribir un programa, llamado rot13.py que reciba un archivo de texto de origen y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo caracter.

def rot13(origen, destino):
    """ caada linea de origen la cifra y la guarda en destino, el cifrado  es:
    a cada caracter comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo caracter
     """
    datos = []
    with open(origen) as forigen:
        lineas = forigen.readlines()
        for linea in lineas:
            lista = linea.split()
            for palabra in lista:
                palabra_codificada = ""
                for letra in palabra:
                    cod_unicode = ord(letra)
                    cod_unicode += 13 
                    cod_unicode = cod_unicode % 26
                    unicode_letra = chr(cod_unicode)
                    palabra_codificada += unicode_letra
                datos.append(palabra_codificada)
    
    with open(destino, "w") as fdestino:
        datos_nuevos = " ".join(datos)
        fdestino.writelines(datos_nuevos)

rot13("lorem.txt", "lorem_cifrado.txt")