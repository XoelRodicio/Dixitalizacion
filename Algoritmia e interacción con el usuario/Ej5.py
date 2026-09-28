#Ordenación de palabras
#El usuario introduce una frase. Muestra las palabras ordenadas alfabéticamente y por longitud.

frase = input("Introduce una frase: ")

palabra = frase.split()

palabra.sort()
print("Ordenación alfabéticamente: ", palabra)

longitud = [len(p) for p in palabra]
longitud.sort()
print("Ordenación por longitud: ", longitud)