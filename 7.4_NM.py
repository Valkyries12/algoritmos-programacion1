#Ejercicio 7.4. Vectores
#a) Escribir una función que reciba dos vectores y devuelva su producto escalar.

def producto_escalar(vec1, vec2):
    """ devuelve el producto escalar de los vectores  """
    total = 0
    for i in range(len(vec1)):
        producto = vec1[i] * vec2[i]
        total += producto
    return total

#print(producto_escalar([-2,1,3], [1,3,2]))

#b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.

def es_ortogonal(vec1, vec2):
    """devuelve si el vector es ortogonal"""
    es_ortogonal = False
    escalar = producto_escalar(vec1, vec2)
    if escalar == 0:
        es_ortogonal = True
    return es_ortogonal

#print(es_ortogonal([2,1], [-1,2]))

#c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.


#d) Escribir una función que reciba un vector y devuelva su norma.