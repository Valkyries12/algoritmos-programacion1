#Ejercicio 7.8. Inversión de listas
#a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

def invierto_copia(lista:list):
    """devuelve una copia de la lista pero invertida  """
    copia = lista[-1::-1]
    return copia

#print(invierto_copia(["Di","buen","dia", "a", "papa"]))
#b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modifique la lista dada para invertirla, sin usar listas auxiliares.

def invierto(lista:list):
    """ devuelve la lista originaal invertida """
    return lista[-1::-1]

print(invierto(["Di","buen","dia", "a", "papa"]))

