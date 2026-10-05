# Diseña una clase Libro y una clase Biblioteca que almacene varios libros en una lista. Implementa métodos para añadir, buscar y listar libros.

class Libro(): 
    def __init__ (self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"Libro tiene el titulo {self.titulo}, su autor es {self.autor} y con ISBN {self.isbn}"

class Biblioteca:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.libros = []

    def añadir(self, *args):
        for l in args:
            self.libros.append(l)
            print(f"Libro '{l.titulo}' añadido correctamente")

    def buscar(self, isbnBuscar):
         if isbnBuscar == self.isbn:
            print(self.libros)
            return self.libros

    def listar(self):
        print("LISTA DE LIBROS")
        for l in self.libros:
            print(l)

if __name__ == "__main__":

    biblioteca = Biblioteca(0)

    libro1 = Libro("El Quijote", "Miguel de Cervantes", 1)
    libro2 = Libro("Mein Kampf", "Adolf Hitler", 2)
    
    biblioteca.añadir(libro1, libro2)

    biblioteca.listar()