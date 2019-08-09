#Ejercicio 2.2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: 𝐹 = 9/5𝐶 + 32

def grados_a_fah(c):
    fah = (9/5)*c +32
    return fah

print(grados_a_fah(6))