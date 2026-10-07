#  Pide al usuario una frase y construye un diccionario con la frecuencia de cada palabra.

frase = input("Introduce una frase: ")

palabras = frase.lower().split()

diccionario = {}

for p in palabras:
    if p in diccionario:
        diccionario[p] += 1
    else:
        diccionario[p] = 1

print(diccionario)
