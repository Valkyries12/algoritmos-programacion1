#Ejercicio 2.1. Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es:
#𝐶𝑛 = 𝐶 × (1 + 𝑥 100 )𝑛
#Donde 𝐶 es el capital inicial, 𝑥 es la tasa de interés y 𝑛 es el número de años a calcular.

def ganancia():
    cantidad_pesos = int(input("Cuandos pesos deposita?: "))
    interes = int(input("Cual es el interes?: "))
    años = int(input("Durante cuantos años?: "))
    ganancia = cantidad_pesos * ((1 + interes/100)**años)
    return ganancia

print(ganancia())