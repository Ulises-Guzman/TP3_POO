print()
print(".: Fundamentos de Clases y Objetos :.")
print()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self, nombre, edad):
        print()
        print("> Los datos de la persona son: ") 
        print(f"    - Nombre: {self.nombre}")
        print(f"    - Edad: {self.edad}")

class Circulo:
    def __init__(self, radio):
        self.radio = int(radio)

    def calcular_area(self, radio):
        PI = 3.14
        area = PI * (radio**2)
        print()
        print("> El área del círculo es: ") 
        print(f"- Area: {round(area, 2)}")

    def calcular_perimetro(self, radio):
        PI = 3.14
        perimetro = 2 * PI * radio
        print()
        print("> El perímetro del círculo es: ") 
        print(f"    - Perímetro: {round(perimetro, 2)}")

class Rectangulo:
    def __init__(self, base, altura):
        self.base = int(base)
        self.altura = int(altura)

    def calcular_area(self, base, altura):
        area = base * altura
        print()
        print("> El área del rectángulo es: ") 
        print(f"    - Area: {round(area, 2)}")

    def calcular_perimetro(self, base, altura):
        perimetro = (base * 2) + (altura * 2)
        print()
        print("> El prímetro del rectángulo es: ") 
        print(f"    - Area: {round(perimetro, 2)}")


# Interacción con usuario, Objeto Persona
print("- Ingrese nombre de la persona y su edad...")
print()
nombre = input("Nombre: ")
edad = input("Edad: ")

persona1 = Persona(nombre, edad)
persona1.mostrar_datos(persona1.nombre, persona1.edad)

print()
print("----------------------------------------------------------------------")

# Interacción con usuario, Objeto Círculo
print()
print("- Ingrese el 'radio' del círulo para calcular su área y perímetro...")
print()
radio = input("Radio: ")

circulo1 = Circulo(radio)
circulo1.calcular_area(circulo1.radio)
circulo1.calcular_perimetro(circulo1.radio)

print()
print("----------------------------------------------------------------------")

# Interacción con usuario, Objeto Rectangulo
print()
print("- Ingrese la 'base' y la 'altura' del retángulo...")
print()
base = input("Base: ")
altura = input("Altura: ")

rectangulo1 = Rectangulo(base, altura)
rectangulo1.calcular_area(rectangulo1.base, rectangulo1.altura)
rectangulo1.calcular_perimetro(rectangulo1.base, rectangulo1.altura)

print()
print("----------------------------------------------------------------------")
