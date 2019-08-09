#Ejercicio 4.2. Escribir una implementación propia de la función abs, que devuelva el valor absoluto de cualquier valor que reciba.

def absoluto(n):
    """ devuelve el valor absoluto """
    absoluto = n
    if n < 0:
        absoluto = n * -1
    return absoluto

print(absoluto(-46))