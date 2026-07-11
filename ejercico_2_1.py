print()
print(".: Métodos Especiales :.")
print()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return (
            f"> Los datos de la persona son: \n"
            f"      - Nombre: {self.nombre} \n"
            f"      - Edad: {self.edad}"
        )

class Circulo:
    def __init__(self, radio, area = 0, perimetro = 0):
        self.radio = radio
        self.area = area
        self.perimetro = perimetro

    def calcular_area(self, radio):
        PI = 3.14
        self.area = PI * (radio**2)


    def calcular_perimetro(self, radio):
        PI = 3.14
        self.perimetro = 2 * PI * radio

    def __str__(self):
        return(
            f"> El área del círculo es: \n"
            f"      - Area: {round(self.area, 2)} \n"
            f"\n"
            f"> El perímetro del círculo es: \n"
            f"      - Perímetro: {round(self.perimetro, 2)}"
        )

class Rectangulo:
    def __init__(self, base, altura, area = 0, perimetro = 0):
        self.base = base
        self.altura = altura
        self.area = area
        self.perimetro = perimetro

    def calcular_area(self, base, altura):
        self.area = base * altura

    def calcular_perimetro(self, base, altura):
        self.perimetro = (base * 2) + (altura * 2)

    def __str__(self):
        return(
            f"> El área del retángulo es: \n"
            f"      - Area: {round(self.area, 2)} \n"
            f"\n"
            f"> El perímetro del retángulo es: \n"
            f"      - Perímetro: {round(self.perimetro, 2)}"
        )

# Interacción con usuario, Objeto Persona
print("- Ingrese nombre de la persona y su edad...")
print()

nombre = input("Nombre: ")
edad = input("Edad: ")
print()

persona1 = Persona(nombre, edad)
print(persona1)

print()
print("----------------------------------------------------------------------")

# Interacción con usuario, Objeto Círculo
print()
print("- Ingrese el 'radio' del círulo para calcular su área y perímetro...")
print()
radio = int(input("Radio: "))

circulo1 = Circulo(radio)
circulo1.calcular_area(circulo1.radio)
circulo1.calcular_perimetro(circulo1.radio)
print(circulo1)

print()
print("----------------------------------------------------------------------")

# Interacción con usuario, Objeto Rectangulo
print()
print("- Ingrese la 'base' y la 'altura' del retángulo...")
print()
base = int(input("Base: "))
altura = int(input("Altura: "))

rectangulo1 = Rectangulo(base, altura)
rectangulo1.calcular_area(rectangulo1.base, rectangulo1.altura)
rectangulo1.calcular_perimetro(rectangulo1.base, rectangulo1.altura)
print(rectangulo1)