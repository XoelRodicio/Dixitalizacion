#Números primos en un rango
#Pide al usuario dos enteros a y b e imprime todos los números primos entre a y b.

a = int(input("Introduce un numero entero: "))
b = int(input("Introduce otro numero entero: "))

for num in range(a, b):
    if num > 1:
        primo = True 
        
        for i in range(2, num):
            if num % i == 0:
                primo = False  
                break            
        
        if primo:
            print(num, end=" ")
