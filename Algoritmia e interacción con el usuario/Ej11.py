# Dado un diccionario con pares clave-valor, crea otro con los valores como claves y las claves como valores.

diccionario = {
    "Xoel" : 20,
    "Gonzokotumbo" : 67
}

diccionarioInverse = {}

for clave,valor in diccionario.items():
    diccionarioInverse[valor] = clave

print("Diccionario: ", diccionario)
print("Diccionario inverso: ", diccionarioInverse)