#Ejercicio 4.1. Escribir dos funciones que resuelvan los siguientes problemas:
#a) Dado un número entero 𝑛, indicar si es par o no.

def es_par(n):
    """ imprime si el numero es par o no """
    if n % 2 == 0:
        print("Es par!")
    else:
        print("No es par")

        
#b) Dado un número entero 𝑛, indicar si es primo o no.



def es_primo(n):
    """ imprime si el numero es primo o no   """
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    if primo == False:
        print(f"{n} no es primo")
    else:
        print(f"{n}  es primo")

#es_par(9)
#es_par(10)
#es_primo(10)
n = int(input("Ingrese un numero"))
for i in range(n):
    es_primo(i)