#Ejercicio 4.5. Escribir funciones que resuelvan los siguientes problemas:
#a) Dado un año indicar si es bisiesto.
#Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

def es_bisiesto(año):
    """ imprime si el año es bisiesto o no   """
    es_bisiesto = ""
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0 :
        es_bisiesto = "es bisiesto"
    else:
        es_bisiesto = "no es bisiesto"
    return es_bisiesto

#es_bisiesto(2024)

#b) Dado un mes, devolver la cantidad de días correspondientes.

def cantidad_dias(mes):
    """ me devuelve la cantidad de dias de un mes especificado  """
    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    dias = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    for i in range(len(meses)):
        if mes == meses[i]:
            cantidad_dias = dias[i]
    return cantidad_dias

#print(f"Junio tiene {cantidad_dias('junio')}")

#c) Dada una fecha (día, mes, año), indicar si es válida o no.

def fecha_valida(dia, mes, año):
    """ devuelve si es valida o no la fecha  """
    valida = None
    if dia <= cantidad_dias(mes):
        valida = "Es válida"
    else:
        valida = "No es válida"
    return valida

#print(fecha_valida(49, "junio", 1987))

#d) Dada una fecha, indicar los días que faltan hasta fin de mes.

def dias_restantes(dia, mes):
    """ devuelve la cantidad de dias que faltan para terminaar el mes  """
    restantes = cantidad_dias(mes) - dia
    return restantes

#print(f"Faltan {dias_restantes(24, 'julio')}")

#e) Dada una fecha, indicar los días que faltan hasta fin de año.

def dias_hasta_fin_anio(dia, mes):
    """ devuelve la cantidad de dias que faltan hastaa fin de año  """
    meses = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    dias = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    acum = 0
    dif_actual = dias[mes] - dia
    for i in range(mes+1, len(meses)):
        acum += dias[i]
    total = acum + dif_actual
    return total

#faltan = dias_hasta_fin_anio(24, 7)
#print(f"Faltan {faltan} dias!")

#f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.

def dias_que_pasaron(dia, mes):
    """ devuelve la cantidad de dias que pasaron  hasta la fecha  """
    meses = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    dias = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    acum = 0
    for i in range(1, mes):
        acum += dias[i]
    total = acum + dia
    return total

#pasaron = dias_que_pasaron(24, 7)
#print(f"pasaron {pasaron} dias")

#g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.
#Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.

def tiempo_transcurrido(dia1, mes1, año1, dia2, mes2, año2):
    """ devuelve la cantidad de dias que pasaron entre dos fechas  """
    acumulador = dias_hasta_fin_anio(dia1, mes1)
    for i in range(año1+1, año2):
        acumulador += 365
    acumulador += dias_que_pasaron(dia2, mes2)
    return acumulador

pasaron = tiempo_transcurrido(14, 2, 2000, 24, 7, 2019)
print(f"Pasaron {pasaron} dias")