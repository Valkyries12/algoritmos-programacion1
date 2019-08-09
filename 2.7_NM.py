#Ejercicio 2.7. Escribir un programa que imprima por pantalla todas las fichas de dominó, de una por línea y sin repetir.

def domino():
    ficha = ""
    for i in range(7):
        for k in range(i, 7):
            ficha = f"|{i} : {k}|"
            print(ficha)

domino()