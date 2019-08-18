#Ejercicio 9.5.3. Continuación de la agenda.
#Escribir un programa que vaya solicitando al usuario que ingrese nombres.
#a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
#b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario puede utilizar la cadena ”*”, para salir del programa.

def agenda():
    diccionario = {}
    sigue = True
    nombre = input("ingrese nombre [* para cerrar]:  ")
    while nombre != "*":
        if nombre in diccionario:
            telefono = input("Desea editar el telefono? [si/no]: ")
            if telefono == "si":
                telefono = int(input("ingrese nuevo numero: "))
                diccionario[nombre] = telefono
        else:
            diccionario[nombre] = []
            telefono = int(input("ingrese el teléfono: "))
            diccionario[nombre].append(telefono)
        nombre = input("ingrese nombre [* para cerrar]:  ")
    return diccionario


print(agenda())