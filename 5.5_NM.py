#Ejercicio 5.5. Algoritmo de Euclides
#a) Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos números 𝑛 y 𝑚, dado por los siguientes pasos.
#1. Teniendo 𝑛 y 𝑚, se obtiene 𝑟, el resto de la división entera de 𝑚/𝑛.
#2. Si 𝑟 es cero, 𝑛 es el mcd de los valores iniciales.
#3. Se reemplaza 𝑚 ← 𝑛, 𝑛 ← 𝑟, y se vuelve al primer paso.
#b) Hacer un seguimiento del algoritmo implementado para los siguientes pares de números: (15, 9); (9, 15); (10, 8); (12, 6).

def mcd(max, min):
    """  devuelve el maximo comun divisor"""
    mcd = 0
    maximo = max
    minimo = min
    while True:
        resto = maximo % minimo
        mcd += maximo // minimo
        maximo = minimo
        minimo = resto
        if maximo % minimo == 0:
            resto = maximo % minimo
            mcd += maximo // minimo
            maximo = minimo
            minimo = resto
            break
    return mcd

def euclides(a, b):
    """  devuelve el maximo comun divisor mediante algoritmo de ueclides"""
    if a > b:
        resultado = mcd(a, b)
    else:
        resultado = mcd(b, a)
    return resultado


print(euclides(1032, 180))