#Ejercicio 3.8.4. Área de un triángulo en base a sus puntos
#a) Escribir una función que reciba las coordenadas de un vector x,y y devuelva la norma
#del vector, dada por ∥(x⃗; y)∥ =
#√
#x2 + y2.
#Ejemplo: norma(3, 4) = 5


from math import sqrt

def norma(x, y):
    """ me devuelve el area de un triangulo dado dos puntos  """
    area = int(sqrt(x**2 + y**2))
    return area

#print(norma(3, 4))


#b) Escribir una función que reciba las coordenadas de dos vectores (x1,y1,x2,y2) y devuelva las coordenadas del vector diferencia (debe devolver un par de valores). Ejemplo: 
# diferencia(8, 7, 5, 3) --> (3, 4)

def diferencia(x1, y1, x2, y2):
    """ Daado coordenadas de dos vectores me devuelve laa diferencia  """
    difX = x1 - x2
    difY = y1 - y2
    return (difX, difY)

#print(diferencia(8, 7, 5, 3))


#c) Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de dos vectores (x1,y1,x2,y2) y devuelva la distancia entre ambos.
#Ejemplo: distancia(8, 7, 5, 3) --> 5

def distancia(x1, y1, x2, y2):
    """devuelve la distancia entre los vectores dado sus valores por parametro"""
    n1, n2 = diferencia(x1, y1, x2, y2)
    resultado = norma(n1, n2)
    return resultado

#print(distancia(8, 7, 5, 3))

#d) Escribir una función que reciba las coordenadas de un vector x,y y devuelva las coordenadas del vector normalizado correspondiente (debe devolver un par de valores).
#Ejemplo: normalizar(3, 4) --> (0.6, 0.8)

def normalizar(x, y):
    """ devuelve las coordenadas del vector normalizado  """
    normalizado = norma(x, y)
    resultadoX = 1 * (x / normalizado)
    resultadoY = 1 * (y / normalizado)
    return (resultadoX, resultadoY)

#print(normalizar(3, 4))

#e) Utilizando las funciones anteriores (b y d), escribir una función que reciba las coordenadas de dos puntos (x1,y1,x2,y2) y devuelva el vector dirección unitario correspondientea la recta que los une.
#Ejemplo: direccion(8, 7, 5, 3) --> (0.6, 0.8)

def direccion(x1, y1, x2, y2):
    """ Devuelve el vector unitario correspondiente laa recta que los une """
    dif1, dif2 = diferencia(x1, y1, x2, y2)
    norma = normalizar(dif1, dif2)
    return norma

#print(direccion(8, 7, 5, 3))

