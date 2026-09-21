#Conversor de temperaturas
#Escribe un programa que pida al usuario una temperatura en grados Celsius y la convierta a Fahrenheit y Kelvin

celsius = int(input("Introduce la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(celsius, "grados Celsius son", fahrenheit, "grados Fahrenheit y", kelvin, "grados Kelvin.")


