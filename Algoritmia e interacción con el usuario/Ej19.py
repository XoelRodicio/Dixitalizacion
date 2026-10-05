# Define una clase Empleado con atributos nombre, sueldo. Hereda Gerente que añade departamento y Programador que añade lenguaje. Implementa un método __str__ adecuado en cada clase.

class Empleado:
    def __init__ (self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleado con nombre: {self.nombre} y sueldo {self.sueldo} "

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return super().__str__() + f"Gerente del departamento {self.departamento}"

class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje):
        super().__init__(nombre,sueldo)
        self.lenguaje = lenguaje

    def __str__(self):
        return super().__str__() + f"Programador en {self.lenguaje}"

if __name__ == "__main__":

    Pepe = Empleado("Pepe", 1000)

    Antonio = Gerente("Antonio", 2000, "Ventas")

    Paco = Programador("Paco", 1500, "Python")

    empleados = [Pepe, Antonio, Paco]

    for e in empleados:
        print(e)