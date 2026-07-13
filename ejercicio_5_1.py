print()
print(".: Ejercicio Integrador :.")
print()

class Usuario:
    def __init__(self, nombre=None, email=None):
        self.__nombre = nombre
        self.__email = email

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, set_nombre):
        self.__nombre = set_nombre
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, set_email):
        self.__email = set_email
    
    def __str__(self):
        return (
            f"-- Usuario: {self.__nombre}, eMail: {self.__email}\n"
            "\n"
            "------------------------------------------------------------------"
            )


class Libro:
    def __init__(self, titulo=None, autor=None, genero=None):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero

    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, set_titulo):
        self.__titulo = set_titulo

    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, set_autor):
        self.__autor = set_autor
    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, set_genero):
        self.__genero = set_genero
    
    def __str__(self):
        return f"-- Libro: '{self.__titulo}, {self.__autor}, Genero: {self.__genero}'"

class Biblioteca:
    libros_prestados = []

    def __init__(self, libros_prestados=[]):
        # Biblioteca.libros = libros
        # Biblioteca.usuarios = usuarios
        Biblioteca.libros_prestados = libros_prestados

    def prestar_libro(self, libro, usuario):
        Biblioteca.libros_prestados.append(libro)
        Biblioteca.libros_prestados.append(usuario)

        print()
        print(f"> Libro {libro.titulo} prestado a usuario {usuario.nombre}")

        print()
        print("> Presione un tecla para continuar...")
        input()
        print()
    
    def devolver_libro(self, libro):
        for indice in range(0, len(self.libros_prestados), 2):
            item = self.libros_prestados[indice]  
            if item.titulo == libro:
                del self.libros_prestados[indice : indice + 1]
                print(f"> Libro {libro} devuelto...")
            break

        
    
    def listar_prestamos(self):
        if len(self.libros_prestados) == 0:
            print()
            print("> No hay libros prestados...")
            print()
            print("> Presione un tecla para continuar...")
            input()
            print()
        else:
            print()
            print("> Lista de libros prestados: ")
            print()

            for item in self.libros_prestados:
                print(item)

            print()
            print("> Presione un tecla para continuar...")
            input()
            print()
            


biblioteca1 = Biblioteca()
# Menu
while True:
    print("\n--- BIBLIOTECA ---\n")
    print("--- MENÚ DE OPCIONES ---\n")
    print("1. Prestar libro")
    print("2. Devolver libro")
    print("3. Listar libros prestados")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        print()
        print("- Ingrese los siguientes datos del libro a prestar...")
        print()
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("genero: ")

        print()
        print("- Ingrese los siguientes datos del usuario que retira el libro...")
        print()
        nombre = input("Nombre: ")
        email = input("eMail: ")

        libro1 = Libro()
        libro1.titulo = titulo
        libro1.autor = autor
        libro1.genero = genero
        
        usuario1 = Usuario()
        usuario1.nombre = nombre
        usuario1.email = email

        biblioteca1.prestar_libro(libro1, usuario1)

    elif opcion == "2":
        print("- Si quiere devolver un libro, ingrese título del libro y nombre del usuario...")
        print()

        titulo = input("Titulo del libro: ")
        # nombre = input("NOmbre de usuario: ")
        biblioteca1.devolver_libro(titulo)

    elif opcion == "3":
        biblioteca1.listar_prestamos()

    elif opcion == "4":
        print()
        print("Saliendo del programa. Vuelvass proonto!")
        break
    else:
        print()
        print("Opción inválida. Por favor, intente de nuevo.")