# Juego de adivinanza
# El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo recibiendo pistas de "mayor" o "menor".

from random import randrange

numRandom = randrange(1,100)

print("ADIVINA EL NUMERO")
while True:
    num = int(input("Introduce el numero que creas que es: "))

    if (num != numRandom):
        if (num > numRandom):
            print("Numero equivocado, el numero es menor")
        else:
            print("Numero equivocado, el numero es mayor")
    else: 
        print("ACERTASTE")
        break