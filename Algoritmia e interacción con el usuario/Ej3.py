#Frecuencia de caracteres
#Pide al usuario una cadena y cuenta cuántas veces aparece cada carácter usando un diccionario.

diccionario = {}
cadena = input("Introduce una cadena de caracteres: ")

for letra in cadena:
    if letra in diccionario:
        diccionario[letra] += 1
    else:
        diccionario[letra] = 1 

for caracter, contar in diccionario.items():
    print(f"El caracter '{caracter}' aparece {contar} veces")