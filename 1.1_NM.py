#Ejercicio 1.10.3. Escribir un programa que pregunte al usuario:
#a) su nombre, y luego lo salude.

def saludo():
    nombre = input("Cual es tu nombre?: ")
    return f"Buenos dias {nombre}"

#b) dos números, y luego muestre el producto.

def producto():
    num1 = int(input("Ingrese primer valor: "))
    num2 = int(input("Ingrese segundo valor: "))
    producto = num1 * num2
    return producto

print(saludo())
print(f"El producto es: {producto()}")