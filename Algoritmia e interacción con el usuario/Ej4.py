#Calculadora básica
#Implementa una calculadora que acepte dos números y una operación (+, -, *, /) introducidos por consola

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

operacion = input("Escribe una operación [+ - * /]: ")

match operacion:
    case "+":
        print("El resultado es", num1 + num2)
    case "-":
        print("El resultado es", num1 - num2)
    case "*":
        print("El resultado es", num1 * num2)
    case "/":
        print("El resultado es", num1 / num2)
    case other:
        print('Error, operación no disponible')

