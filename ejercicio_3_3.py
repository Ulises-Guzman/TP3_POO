print()
print(".: Jerarquía :.")
print()

class Vehiculo:
    def __init__(self, marca=None, modelo=None, anio=None):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    # Getter
    @property
    def marca(self):
        return self.__marca
    
    # Setter
    @marca.setter
    def marca(self, nueva_marca):
        self.__marca = nueva_marca

    # Getter
    @property
    def modelo(self):
        return self.__modelo
    
    # Setter
    @modelo.setter
    def modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    # Getter
    @property
    def anio(self):
        return self.__anio
    
    # Setter
    @anio.setter
    def anio(self, nuevo_anio):
        self.__anio = nuevo_anio

    def encender(self, opcion):
        if opcion == "on":
            return print("> El vehículo se encendió...")

    def apagar(self, opcion):
        if opcion == "on":
            return print("> El ve´hiculo se apagó...")

class Auto(Vehiculo):
    def __init__(self, marca=None, modelo=None, anio=None, dominio=None, color=None):
        super().__init__(marca, modelo, anio)
        self.__dominio = dominio
        self.__color = color

    # Getter
    @property
    def dominio(self):
        return self.__dominio
    
    # Setter
    @dominio.setter
    def dominio(self, nuevo_dominio):
        self.__dominio = nuevo_dominio

    # Getter
    @property
    def color(self):
        return self.__color
    
    # Setter
    @color.setter
    def color(self, nuevo_color):
        self.__color = nuevo_color

    def activar_nitro(self, opcion):
        if opcion == "on":
            return print("> Se activó nitro...")
        else:
            return print("> Se desactivó modo nitro...")
            

    def activar_velocidad_crucero(self, opcion):
        if opcion == "on":
            return print("> Se activó modo velocidad crucero...")
        else:
            return print("> Se desactivó modo velocidad crucero...")


class Moto(Vehiculo):
    def __init__(self, marca=None, modelo=None, anio=None, dominio=None, color=None):
        super().__init__(marca, modelo, anio)
        self.__dominio = dominio
        self.__color = color

    # Getter
    @property
    def dominio(self):
        return self.__dominio
    
    # Setter
    @dominio.setter
    def dominio(self, nuevo_dominio):
        self.__dominio = nuevo_dominio

    # Getter
    @property
    def color(self):
        return self.__color
    
    # Setter
    @color.setter
    def color(self, nuevo_color):
        self.__color = nuevo_color

    def activar_potencia(self, opcion):
        if opcion == "on":
            return print("> Se activó modo alta potencia...")
        else:
            return print("> Se desactivó modo alta potencia...")

# Interacción con usuario
print("- Ingrese los siguientes datos del auto...")
print()

marca = input("Marca: ")
modelo = input("Modelo: ")
anio = input("Año:")
dominio = input("Dominio: ")
color = input("Color: ")

auto1 = Auto()
auto1.marca = marca
auto1.modelo = modelo
auto1.anio = anio
auto1.dominio = dominio
auto1.color = color

print()
print("- Encender el auto?...")
print()
encender_auto = input("On/Off: ").lower()

print()
print("- Activar o desactivar modo nitro...")
print()
nitro = input("On/Off: ").lower()

# Salida de estado Auto
print()
print("> Los datos del auto son: ")
print(f"    - Marca : {auto1.marca}")
print(f"    - Modelo : {auto1.modelo}")
print(f"    - Año : {auto1.anio}")
print(f"    - Dominio : {auto1.dominio}")
print(f"    - Color : {auto1.color}")

print()
auto1.encender(encender_auto)

print()
print("> Modo: ")
auto1.activar_nitro(nitro)

# Interacción con usuario
print()
print("- Ingrese los siguientes datos de la moto...")
print()

marca = input("Marca: ")
modelo = input("Modelo: ")
anio = input("Año:")
dominio = input("Dominio: ")
color = input("Color: ")

moto1 = Moto()
moto1.marca = marca
moto1.modelo = modelo
moto1.anio = anio
moto1.dominio = dominio
moto1.color = color

print()
print("- Encender la moto?...")
print()
encender_moto = input("On/Off: ").lower()

print()
print("- Activar o desactivar modo alta potencia...")
print()
alta_potencia = input("On/Off: ").lower()

# Salida de estado Moto
print()
print("> Los datos de la moto son: ")
print(f"    - Marca : {moto1.marca}")
print(f"    - Modelo : {moto1.modelo}")
print(f"    - Año : {moto1.anio}")
print(f"    - Dominio : {moto1.dominio}")
print(f"    - Color : {moto1.color}")

print()
moto1.encender(encender_moto)

print()
print("> Modo: ")
moto1.activar_potencia(alta_potencia)