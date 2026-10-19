# Escribe un programa que calcule el producto de todos los números de una lista usando reduce.
# Ejemplo:

# Entrada → [2, 3, 4]
# Salida → 24

from functools import reduce

def multiplicar(acum, num):
    return acum * num

numeros = [2, 3, 4]

resultado = reduce(multiplicar, numeros)

print(resultado)