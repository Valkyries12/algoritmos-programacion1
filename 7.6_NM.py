#Ejercicio 7.6 Dada una lista de números enteros y un entero k, escribir una función que:
#a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
def tres_listas(numeros:list, num:int):
    """ Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.  """
    menores = []
    mayores = []
    iguales = []
    for numero in numeros:
        if numero < num:
            menores.append(numero)
        elif numero > num:
            mayores.append(numero)
        else:
            iguales.append(numero)
    return (menores, mayores, iguales)

#resultado = tres_listas([5,6,7,8,9,10], 7)
#print(resultado)


#b) Devuelva una lista con aquellos que son múltiplos de k.
def multiplos(numeros:list, k:int):
    """ devuelve una lista con los que son multiplos de k  """
    lista_multiplos = []
    for numero in numeros:
        if numero % k == 0:
            lista_multiplos.append(numero)
    return lista_multiplos

resultado = multiplos([3,4,5,10,15,16,17,20], 5)
print(resultado)