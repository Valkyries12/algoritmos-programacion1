#Ejercicio 3.1. Escribir dos funciones que permitan calcular:
#a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
#b) La duración en horas, minutos y segundos de un intervalo dado en segundos.

def convierte_a_segundos(horas, minutos, segundos):
    """ convierte a segundos los parametros dados en formato hora, minutos, segundos """
    return 3600 * horas + 60 * minutos + segundos

def conversion_a_horas(segundos):
    """  devuelve en formato hh mm ss lo pasado en segundos por parametros """
    horas = segundos // 3600
    minutos = segundos // 60
    seg = segundos
    return f"{segundos} son {horas} hora, {minutos} minutos, {seg} segundos"

print(convierte_a_segundos(6, 17, 5))
print(conversion_a_horas(456789))
help(conversion_a_horas)
help(convierte_a_segundos)