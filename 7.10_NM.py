#Ejercicio 7.10. Matrices.

def suma_matriz(matriz):
    """ devuelve la suma de una matriz  """
    suma = 0
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            suma += matriz[i][k]
    return suma

#print(suma_matriz([[2,3], [10,15], [20,20], [40,40]]))



#a) Escribir una función que reciba dos matrices y devuelva la suma.
matriz = [[2,3], [10,15], [20,20], [40,40]]
def suma_matrices(matriz1, matriz2):
    """ devuelve la suma de dos matrices """
    mat1 = suma_matriz(matriz1)
    mat2 = suma_matriz(matriz2)
    total = mat1 + mat2
    return total

#print(suma_matrices(matriz, matriz))


#b) Escribir una función que reciba dos matrices y devuelva el producto.

def producto_matrices(matriz1, matriz2):
    """ devuelve el producto de las dos matrices """
    mat1 = suma_matriz(matriz1)
    mat2 = suma_matriz(matriz2)
    total = mat1 * mat2
    return total

#print(producto_matrices(matriz, matriz))


#c) ⋆ Escribir una función que opere sobre una matriz y mediante eliminación gaussiana devuelva una matriz triangular superior.


#d) ⋆ Escribir una función que indique si un grupo de vectores, recibidos mediante una lista, son linealmente independientes o no.

