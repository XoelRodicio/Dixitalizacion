# Implementa una clase Cuenta con saldo inicial y métodos para ingresar, retirar y mostrar saldo. Añade control de fondos insuficientes.

class Cuenta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"Error: Fondos insuficientes")
        elif cantidad <= 0:
            print("Error: La cantidad a retirar debe ser mayor que 0")
        else:
            self.saldo -= cantidad

    def mostrar_saldo(self):
        print(f"Saldo disponible: {self.saldo}€")
        return self.saldo

if __name__ == "__main__":
    cuenta = Cuenta(0)

    ingreso = int(input("Introduce la cantidad que desees ingresar: "))
    cuenta.ingresar(ingreso)

    retiro = int(input("Introduce la cantidad que desees retirar: "))
    cuenta.retirar(retiro)
    
    cuenta.mostrar_saldo()
