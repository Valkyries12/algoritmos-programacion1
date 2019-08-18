#Ejercicio 10.7. Persistencia de un diccionario
#a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave y el segundo como valor.

def cargar_datos(archivo):
    """ devuelve un diccionario con los usuarios y contraseñas del archivo leido  """
    diccionario = {}
    with open(archivo) as f:
        lineas = f.readlines()
        for linea in lineas:
            lista = linea.split()
            for palabra in lista:
                diccionario[lista[0]] = lista[1]
    return diccionario


print(cargar_datos("usuarios_contrasenas.txt"))


#b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo, y guarde el contenido del diccionario en el archivo, con el formato clave, valor.

def guardar_datos(archivo, diccionario:dict):
    """ recibe un diccionario con usuario y contraseñas y guarda esos valores en el archivo destino """
    with open("guardar_datos" , "a") as f:
        for key, value in diccionario.items():
            datos = f"{key} {value}"
            f.write(f"{datos} \n")

users = {
    "nicolas12" : "12345",
    "elefante17" : "linterna",
    "maxi19" : "superman"
}

guardar_datos("guardar_datos.txt", users)