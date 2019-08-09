#Ejercicio 1.6. Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, en una única línea, con espacios intermedios.
#Ayuda: Investigar acerca del parámetro end de la función print.

def imprime_mil_veces(palabra):
    for i in range(1000):
        print(palabra, end=" ")

imprime_mil_veces("elefante")
