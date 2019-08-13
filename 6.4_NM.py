#Ejercicio 6.4. Escribir una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'.

def separaciones_miles(cadena):
    """ devuelve una cadena con el numero y sus separaciones en miles  """
    sub = ""
    completa = ""
    espejo = cadena[-1::-1]
    for letra in espejo:
        sub += letra
        if len(sub) == 3:
            sub += "."
            completa += sub
            sub = ""
    completa += sub
    completa = completa[-1::-1]
    return completa

print(separaciones_miles("1234567890"))