#Gestión de notas
#Solicita al usuario nombres y calificaciones de varios alumnos (hasta que escriba "fin"). Al final muestra:
#Nota media
#Nota más alta
#Nota más baja

lista = {}
nombres = ""

while True:
    nombres = input("Introduce el nombre del alumno: ")
    if nombres == "fin":
            break

    calificaciones = []
    while True:
        notas = input("Introduce las calificaciones: ")
        
        if notas == "":
            break 
        
        calificaciones.append(float(notas))
        

    lista[nombres] = calificaciones
    

print(lista)


