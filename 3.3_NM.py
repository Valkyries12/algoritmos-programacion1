#Ejercicio 3.3. Escribir una función que, dados cuatro números, devuelva el mayor producto de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más grande que se puede obtener entre ellos (8 = −2 × −4).

def mayor_producto_entre_dos(n1, n2, n3, n4):
    """ me devuelve el mayor producto entre los numeros especificados por parametro """
    mayor = n1 * n2
    if n3 * n4 > mayor:
        mayor = n3 * n4
    return mayor
    

print(mayor_producto_entre_dos(1, 5, -2, -4))