#Gestión de notas
#Solicita al usuario nombres y calificaciones de varios alumnos (hasta que escriba "fin"). Al final muestra:
#Nota media
#Nota más alta
#Nota más baja

# Gestión de notas
lista = {}
todasNotas = []

while True:
    nombres = input("Introduce el nombre del alumno: ")
    if nombres == "fin":
        break

    calificaciones = [] 
    while True:
        notas = input("Introduce una calificación: ")
        if notas == "":
            break 

        nota = float(notas)
        calificaciones.append(nota)
        todasNotas.append(nota)  
        
    lista[nombres] = calificaciones

if todasNotas:
    notaMax = max(todasNotas)
    notaMin = min(todasNotas)
    notaMedia = sum(todasNotas) / len(todasNotas)

    print(f"Nota media: {notaMedia:.2f}")
    print(f"Nota más alta: {notaMax}")
    print(f"Nota más baja: {notaMin}")
    print(lista)
else:
    print("No se introdujeron calificaciones.")



