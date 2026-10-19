#  Crea una función que reciba una lista de números y devuelva el mínimo, el máximo y la media.
#  Ejemplo:

# Entrada → [4, 7, 1, 9]
# Salida → (1, 9, 5.25)

entrada = [4,7,1,9]

def numeros(lista):
    maximo = lista[0] 
    
    for n in lista:
        if n > maximo:
            maximo = n 

    minimo = lista[0]

    for n in lista:
        if n < minimo:
            minimo = n

    total = 0

    for n in lista:
        total = total + n

    media = total / len(entrada)
    
    return minimo, maximo, media
    
print(numeros(entrada))