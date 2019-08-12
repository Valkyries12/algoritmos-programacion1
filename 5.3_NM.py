#Ejercicio 5.3. Manejo de contraseñas
#a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
#b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
#c) Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función sleep del módulo time.
#d) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

import time

def verificar_contrasenia(password):
    """ repite la introuccion de la pw mientras la contraseña no sea correcta  """
    ingresar_pw = input("Ingrese contraseña: ")
    while ingresar_pw != password:
        ingresar_pw = input("Ingrese correctamente la contraseña: ")
    print("contraseña correcta!!!")

def verificar_contrasenia2(password):
    """ repite la introuccion de la pw hasta 3 intentos """
    intentos = 0
    ingresar_pw = input("ingrese contraseña [tiene tres intentos]: ")
    while ingresar_pw != password:
        intentos += 1
        ingresar_pw = input("ingrese contraseña: ")
        if intentos == 3:
            print("Error! ha intentado loguearse mas de 3 veces incorrectamente")
            return
    print("Bienvenido")

def verificar_contrasenia3(password):
    """ cada vez que se introduce mal la contraseña se alarga el tiempo de espera en 1 seg """
    segundos = 0
    ingresar_pw = input("ingrese la contraseña: ")
    while ingresar_pw != password:
        print(f"Contraseña incorrecta espere {segundos} segundos")
        time.sleep(segundos)
        segundos += 1
        ingresar_pw = input("Ingrese contraseña: ")
    print("Bienvenido")

def verificar_contrasenia4(password):
    """ me devuelve true o false dependiendo si se puso o no la contraseña correctamente  """
    ingresar_pw = input("ingrese contraseña: ")
    if ingresar_pw != password:
        return False
    else:
        return True
#verificar_contrasenia("mactolos")
#verificar_contrasenia2("mactolos")
#verificar_contrasenia3("mactolos")
print(verificar_contrasenia4("mactolos"))