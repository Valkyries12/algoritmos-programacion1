#Ejercicio 2.8. Modificar el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a 𝑛.

def domino():
    cantidad = int(input("ccual es la pieza con mayor puntos?: "))
    ficha = ""
    for i in range(cantidad+1):
        for k in range(i, cantidad+1):
            ficha = f"|{i} : {k}|"
            print(ficha)

domino()