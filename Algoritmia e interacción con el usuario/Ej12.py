#  Crea un programa que guarde contactos en un diccionario con nombre y una lista de  teléfonos. Permite añadir y buscar contactos por nombre.

diccionario = {
    "Gonzokotumbo" : 666443322,
    "Consuela" : 222334466
}

while True: 
    print("""
    MENU
    1- AÑADIR CONTACTO
    2- BUSCAR CONTACTO
    3- SALIR
    """)

    menu = input("Que deseas hacer: ")

    if menu == "1":
        print("Hola")
    elif menu == "2": 
        print("BUSCAR CONTACTOS POR NOMBRE")
        buscar = input("Introduce el nombre del contacto: ")
        for clave, valor in diccionario.items():
            if buscar == valor:
                print("si")
            else: print("no")
    elif menu == "3":
        print("Saliendo")
        break 
    else:
        print("Opción no válida")
