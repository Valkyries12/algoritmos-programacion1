#Ejercicio 2.5. Escribir un programa que le pregunte al usuario un número 𝑛 e imprima los primeros 𝑛 números triangulares, junto con su índice. Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta 𝑛.

def numero_triangular(n):
    arr = [0]
    for i in range(1, n+1):
        arr.append(i + arr[i-1])
        print(f"{i} - {arr[i]}")

numero_triangular(5)