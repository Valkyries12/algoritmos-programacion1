#Ejercicio 6.8. Escribir una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria) y devuelva el valor decimal correspondiente.

def a_decimal(cadenaBinario):
    """devuelve el valor en decimal"""
    binario = cadenaBinario[-1::-1]
    total = 0
    potencia = 0
    for digito in binario:
        if int(digito) == 1:
            total += (int(digito)*2) ** potencia
        potencia += 1
    return total

print(a_decimal("1011"))
