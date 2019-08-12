#Ejercicio 5.3. Nos piden que escribamos una función que le pida al usuario que ingrese un número positivo. Si el usuario ingresa cualquier cosa que no sea lo pedido se le debe informar de su error mediante un mensaje y volverle a pedir el número.
#Resolver este problema usando
#1. Un ciclo interactivo.
#2. Un ciclo con centinela.
#3. Un ciclo “infinito” que se corta.

def repite_hasta():
    numero = int(input("ingrese un numero positivo: "))
    while numero < 0:
        print("Error")
        numero = int(input("Ingrese numero positivo: "))

def repite_hasta_centinela():
    centinela = input("Ingrese un numero positivo <* para terminar>: ")
    while centinela != "*":
        x = int(centinela)
        if x > 0:
            print("Numero positivo")
        else:
            print("Error")
        centinela = input("Ingrese numero positivo <* para terminar>: ")
    print("Terminado")


def infinito_cortado():
    while True:
        numero = input("Ingrese un numero positivo <* para terminar>: ")
        if numero == "*":
            print("Terminado")
            break
        else:
            x = int(numero)
            if x > 0:
                print("positivo")
            else:
                print("Error")
                


#repite_hasta()
#repite_hasta_centinela()
infinito_cortado()