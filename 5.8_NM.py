#Ejercicio 5.8. Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.

def sucesion():
    """ imprime cantidad de numeros ingresados, suma y promedio de los valores puestos"""
    numero = 0
    cantidad_ingresados = 0
    suma = 0
    promedio = 0
    numero = int(input("Ingrese un numero natural [-1 para salir]: "))
    while numero > -1:
        cantidad_ingresados += 1
        suma += numero
        promedio = suma // cantidad_ingresados
        numero = int(input("Ingrese un numero natural [-1 para salir]: "))
    print(f"cantidad ingresados: {cantidad_ingresados}")
    print(f"suma: {suma}")
    print(f"promedio: {promedio}")

sucesion()