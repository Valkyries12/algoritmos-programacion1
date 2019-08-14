#Ejercicio 7.3. Campaña electoral
#a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el mensaje Estimado <nombre>, vote por mí.


def campaña_electoral(tupla):
    """ imprime el texto usando los nombres de la tupla dada """
    for nombre in tupla:
        print(f"Estimado {nombre} vote por mi")

#campaña_electoral(("Nicolas", "Marcelo", "Rodolfo"))

#b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición p.

def campaña_electoral2(nombres, origen, cantidad):
    """ imprime el mensaje usando los nombres a partir de una posicion especificada  """
    for i in range(origen, cantidad):
        print(f"Estimado {nombres[i]} vote por mi")

#campaña_electoral2(("Nicolas", "Alfonzo", "Edgardo", "Maria", "Lucrecia"), 1,3)
#c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario, para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.

def campaña_electoral3(nombres):
    for nombre in nombres:
        if nombre[0] == "masculino":
            print(f"Estimado {nombre[1]} vote por mi")
        if nombre[0] == "femenino":
            print(f"Estimada {nombre[1]} vote por mi")

nombres = (("femenino", "Maria"), ("masculino", "Nicolás"), ("masculino", "Iván"), ("femenino", "Julieta"))
campaña_electoral3(nombres)