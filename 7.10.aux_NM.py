#Ejercicio 7.10. Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su oficina cortando todas las palabras de más de cinco letras a sólo cinco letras (e indicando que una palabra fue cortada con el agregado de una arroba). Además elimina todos los espacios en blanco de más. Por ejemplo, al texto " Llego mañana alrededor del mediodía " se transcribecomo "Llego mañan@ alred@ del medio@".Por otro lado cobra un valor para las palabras cortas y otro valor para las palabras largas(que deben ser cortadas).
#a) Escribir una función que reciba un texto, la longitud máxima de las palabras, el costo de cada palabra corta, el costo de cada palabra larga, y devuelva como resultado el texto deltelegrama y el costo del mismo.
#b) Los puntos se reemplazan por la palabra especial ”STOP”, y el punto final (que puede faltar en el texto original) se indica como ”STOPSTOP”.
#Al texto:
#" Llego mañana alrededor del mediodía. Voy a almorzar "
#Se lo transcribe como:
#"Llego mañan@ alred@ del medio@ STOP Voy a almor@ STOPSTOP".

def procesar_telegrama(texto, longitud_palabras, valorCortas, valorLargas):
    """ procesa el telegrama  """
    texto_a_lista = texto.split()
    lista_a_texto = []
    cantidad_largas = 0
    cantidad_cortas = 0
    total_largas = 0
    total_cortas = 0
    for elemento in texto_a_lista:
        if len(elemento) > longitud_palabras:
            cortar = elemento[0:longitud_palabras]
            cortar += "@"
            lista_a_texto.append(cortar)
            cantidad_largas += 1
        else:
            lista_a_texto.append(elemento)
            cantidad_cortas += 1
    total_cortas = cantidad_cortas * valorCortas
    total_largas = cantidad_largas * valorLargas
    lista_a_texto = " ".join(lista_a_texto)
    return f"{lista_a_texto} cuesta {total_cortas + total_largas}$"

print(procesar_telegrama("Llego mañana alrededor del mediodía. Voy a almorzar", 5, 1.45, 3.45))