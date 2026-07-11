print()
print(".: Composición y Agregación :.")
print()

class Estudiante:
    def __init__(self, apellido=None, nombre=None, dni=None, carrera=None, anio=None):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__carrera = carrera
        self.__anio = anio

    # Getter
    @property
    def apellido(self):
        return self.apellido
    
    # Setter
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido

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
    def dni(self):
        return self.__dni
    
    # Setter
    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni

    # Getter
    @property
    def carrera(self):
        return self.__carrera
    
    # Setter
    @carrera.setter
    def carrera(self, nueva_carrera):
        self.__carrera = nueva_carrera

    # Getter
    @property
    def anio(self):
        return self.__anio
    
    # Setter
    @anio.setter
    def anio(self, nuevo_anio):
        self.__anio = nuevo_anio

    def __str__(self):
        return f"-- {self.__apellido}, {self.__nombre} | {self.__dni} | {self.__carrera} | {self.__anio} --"


class Curso:
    estudiantes = []
    def __init__(self, estudiantes=[]):
        Curso.estudiantes = estudiantes

    def agregar_estudiante(self, estudiante):
        Curso.estudiantes.append(estudiante)

    def mostrar_curso(self):
        print("> Curso completo: ")
        print()
        for estudiante in Curso.estudiantes:
            print(estudiante)

# Interacción con usuario
print("- Ingrese los siguientes datos del estudiante...")
print("> Nota: Se corta la carga de datos con Apellido = 0")
print()

curso1 = Curso()

apellido = input("Apellido: ")
while apellido != "0": 
    nombre = input("Nombre: ")
    dni = input("DNI:")
    carrera = input("Carrera: ")
    anio = input("Año: ")

    estudiante1 = Estudiante()
    estudiante1.apellido = apellido
    estudiante1.nombre = nombre
    estudiante1.dni = dni
    estudiante1.carrera = carrera
    estudiante1.anio = anio

    curso1.agregar_estudiante(estudiante1)
    print("> Estudiante agregado: ")
    print(estudiante1)

    print()
    print("- Ingrese los datos del siguiente estudiante...")
    apellido = input("Apellido: ")

print("> Finalizada la carga de datos...")
print()
curso1.mostrar_curso()
print()