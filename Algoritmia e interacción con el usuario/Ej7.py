#Gestión de notas
#Solicita al usuario nombres y calificaciones de varios alumnos (hasta que escriba "fin"). Al final muestra:
#Nota media
#Nota más alta
#Nota más baja

# Gestión de notas
lista = {}
todas_las_notas = []  # <--- Nueva lista para acumular TODAS las notas de la clase

while True:
    nombres = input("Introduce el nombre del alumno (o 'fin' para terminar): ")
    if nombres.lower() == "fin":
        break

    calificaciones_alumno = [] 
    while True:
        notas = input(f"Introduce una calificación para {nombres} (enter para terminar): ")
        if notas == "":
            break 

        nota_numerica = float(notas)
        calificaciones_alumno.append(nota_numerica)
        todas_las_notas.append(nota_numerica)  
        
    lista[nombres] = calificaciones_alumno

if todas_las_notas:
    notaMax = max(todas_las_notas)
    notaMin = min(todas_las_notas)
    notaMedia = sum(todas_las_notas) / len(todas_las_notas)

    print("\n--- RESULTADOS GLOBALES ---")
    print(f"Nota media de la clase: {notaMedia:.2f}")
    print(f"Nota más alta: {notaMax}")
    print(f"Nota más baja: {notaMin}")
    print("\nDiccionario completo de alumnos:", lista)
else:
    print("No se introdujeron calificaciones.")



