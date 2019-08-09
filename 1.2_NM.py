#Ejercicio 1.10.4. Implementar algoritmos que permitan:
#a) Calcular el perímetro de un rectángulo dada su base y su altura.
from math import sqrt

def perimetro_rectangulo(base, altura):
    perimetro = base * 2 + altura * 2
    return perimetro

#b) Calcular el área de un rectángulo dada su base y su altura.

def area_rectangulo(base, altura):
    area = base * altura
    return area


#d) Calcular el perímetro de un círculo dado su radio.

def perimetro_circulo(radio):
    perimetro = 2*3.14 * radio
    return perimetro

#e) Calcular el área de un círculo dado su radio.

def area_circulo(radio):
    area = 3.14 * radio**2
    return area

#f) Calcular el volumen de una esfera dado su radio.


def volumen(radio):
    volumen = (4/3) * 3.14 * radio**3
    return volumen

#g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.


def hipotenusa(cateto1, cateto2):
    hipotenusa = sqrt((cateto1 ** 2 + cateto2 ** 2))
    return hipotenusa

