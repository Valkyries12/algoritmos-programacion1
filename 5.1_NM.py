#Ejercicio 5.1. Escribir un programa que permita al usuario ingresar un conjunto de notas, preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

def notas():
    notas = "si"
    cont = 0
    acum_nota = 0
    while notas == "si":
        nota = int(input("Ingrese nota: "))
        acum_nota += nota
        cont += 1
        promedio = acum_nota // cont
        notas = input("Desea ingresar mas notas? [si / no]: ")
    return promedio

print(notas())