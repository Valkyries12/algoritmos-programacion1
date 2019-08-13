#Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
#a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver 's,e,p,a,r,a,r'

def entre_medio(cadena, caracter):
    """ devuelve la palabra con cada caracter insertado entre todas sus letras  """
    completo = ""
    for letra in cadena:
        completo += f"{letra}{caracter}"
    return completo

#print(entre_medio("elefante", "-"))

#b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_' debería devolver 'mi_archivo_de_texto.txt'

def reemplaza_espacios(cadena, caracter):
    """ reemplaza todos los espacios en blanco por el caracter dado  """
    completo = ""
    for letra in cadena:
        if letra == " ":
            letra = caracter
        completo += letra
    return completo

#print(reemplaza_espacios("mi archivo de texto.txt", "_"))

#c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y 'X' debería devolver 'su clave es: XXXX'

def reemplaza_digitos(cadena, caracter):
    """ reemplaza todos los digitos por el caracter dado """
    completo = ""
    for letra in cadena:
        if letra.isdigit():
            letra = caracter
        completo += letra
    return completo

#print(reemplaza_digitos("L1nt3rn4", "*"))

#d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver '255.255.255.0'

def cada_tres_digitos(cadena, caracter):
    """ inserta el caracter cada tres digitos  """
    completo = ""
    sub = ""
    for letra in cadena:
        sub += letra
        if len(sub) % 3 == 0:
            completo += sub + "."
            sub = ""
    completo += letra
    return completo

print(cada_tres_digitos("2552552551", "."))
