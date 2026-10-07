# Tuplas y coordenadas Pide al usuario dos puntos (x, y) y calcula la distancia euclidiana entre ellos.
import math

coordX = float(input("Introduce la coordenada X1: "))
coordY = float(input("Introduce la coordenada Y1: "))


puntoX = (coordX, coordY)

coordX2 = float(input("Introduce la coordenada X2: "))
coordY2 = float(input("Introduce la coordenada Y2: "))

puntoY = (coordX2, coordY2)

distancia = math.dist(puntoX, puntoY)

print(f"La distancia euclidiana es {distancia}")

