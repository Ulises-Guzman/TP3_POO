print()
print(".: Herencia :.")
print()

class Persona:
    def __init__(self, nombre=None, edad=None):
        self.__nombre = nombre
        self.__edad = edad

    # Getter
    @property
    def nombre(self):
        return self.__nombre

    # Setter
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Getter
    @property
    def edad(self):
        return self.__edad

    # Setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

class Estudiante(Persona):
    def __init__(self, nombre=None, edad=None, curso=None, nota_final=None):
        super().__init__(nombre, edad)
        self.__curso = curso
        self.__nota_final = nota_final

    # Getter
    @property
    def curso(self):
        return self.__curso
    
    # Setter
    def curso(self, nuevo_curso):
        self.__curso = nuevo_curso

    # Getter
    @property
    def nota_final(self):
        return self.__nota_final

    # Setter
    def nota_final(self, nueva_nota):
        self.__nota_final = nueva_nota

print("- Ingrese los siguientes datos del estudiante...")
print()
nombre = input("Nombre: ")
edad = input("Edad: ")
curso = input("Curso: ")
nota_final = input("Nota final: ")

estudiante1 = Estudiante()
estudiante1.nombre = nombre
estudiante1.edad = edad
estudiante1.curso = curso
estudiante1.nota_final = nota_final

print()
print("> Los datos del estudiante son: ")
print(f"    - Nombre : {estudiante1.nombre}")
print(f"    - Edad : {estudiante1.edad}")
print(f"    - Curso : {estudiante1.curso}")
print(f"    - Nota Final : {estudiante1.nota_final}")




