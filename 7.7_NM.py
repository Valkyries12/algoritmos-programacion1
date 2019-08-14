#Ejercicio 7.7. Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el nombre, luego la inicial con un punto, y luego el apellido.

def nombre_completo(nombres:list):
    """Devuelve una lista de cadenas con el nombre completo, inicial segundo nombre y apellido"""
    nombre_completo = []
    aux = ""
    for nombre in nombres:
        aux += f"{nombre[1]} {nombre[2]}. {nombre[0]}"
        nombre_completo.append(aux)
        aux = ""
    return nombre_completo

lista = [("Caruso", "Nicolás", "M"),("Lopez","Juan","M"),("Gaulhofer","Gustavo", "G"),("Higa", "Juan","M")]
print(nombre_completo(lista))
