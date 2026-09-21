#Números pares e impares
#Solicita al usuario una lista de números separados por espacios y muestra dos listas: una con los pares y otra con los impares

numeros = list(map(int,input("Escribe números separados por espacios: ").split()))

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print(f"Pares: {pares}")
print(f"Impares: {impares}")