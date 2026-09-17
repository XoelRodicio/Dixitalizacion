entrada = input("Escribe números separados por espacios: ")

num = entrada.split()

pares = []
impares = []

for elemento in num:
    numero = int(elemento)
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Pares:", pares)
print("Impares:", impares)