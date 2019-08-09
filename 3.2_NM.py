#Ejercicio 3.2. Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

def convierte_a_segundos(horas, minutos, segundos):
    """ convierte a segundos los parametros dados en formato hora, minutos, segundos """
    return 3600 * horas + 60 * minutos + segundos

def conversion_a_horas(segundos):
    """  devuelve en formato hh mm ss lo pasado en segundos por parametros """
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seg = (segundos % 3600) % 60
    return f"{segundos} son {horas} hora, {minutos} minutos, {seg} segundos"

def intervalo(intervalo1, intervalo2):
    """ se recibe dos intervalos de horas convertidos a segudnos y me devuelvo la suma de ellos  """
    suma = intervalo1 + intervalo2
    return conversion_a_horas(suma)
    

intervalo1 = convierte_a_segundos(4, 56, 23)
intervalo2 = convierte_a_segundos(10, 34, 12)
print(intervalo(intervalo1, intervalo2))