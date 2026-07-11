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

class Empleado(Persona):
    def __init__(self, nombre=None, edad=None, sueldo=None):
        super().__init__(nombre, edad)
        self.__sueldo = sueldo

    # Getter
    @property
    def sueldo(self):
        return self.__sueldo
    
    # Setter
    @sueldo.setter
    def sueldo(self, nuevoSueldo):
        self.__sueldo = nuevoSueldo

    def calculo_bonificaciones(self, sueldo, bonificacion ):
        sueldo_total = sueldo + (sueldo * (bonificacion/100))
        return sueldo_total

print("- Ingrese los siguientes datos del empleado...")
print()
nombre = input("Nombre: ")
edad = input("Edad: ")
sueldo = float(input("Sueldo($): "))
bonificacion = float(input("Bonificacion(%): "))

empleado1 = Empleado()
empleado1.nombre = nombre
empleado1.edad = edad
empleado1.sueldo = sueldo

sueldo_bonificado = empleado1.calculo_bonificaciones(empleado1.sueldo, bonificacion)

print()
print("> Los datos del empleado son: ")
print(f"    - Nombre : {empleado1.nombre}")
print(f"    - Edad : {empleado1.edad}")
print(f"    - Sueldo : {empleado1.sueldo}")
print(f"    - Bonificación : +{round(bonificacion, 2)}%")
print(f"    - Sueldo bonificado : ${round(sueldo_bonificado)}")