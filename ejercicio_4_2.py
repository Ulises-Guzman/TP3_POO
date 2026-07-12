print()
print(".: Composición y Agregación :.")
print()

class Producto:
    def __init__(self, nombre=None, categoria=None, precio=None, cantidad=None):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

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
    def categoria(self):
        return self.__categoria
    
    # Setter
    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = nueva_categoria

    # Getter
    @property
    def precio(self):
        return self.__precio

    # Setter
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    # Getter
    @property
    def cantidad(self):
        return self.__cantidad
    
    # Setter
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad

    def __str__(self):
        return f"Producto: -- | {self.__nombre} | Categoria: {self.__categoria} | Precio: {self.__precio} | Cantidad: {self.__cantidad} --"

class Tienda:
    def __init__(self):
        self.__productos = []
    
    def agregar_producto(self, nuevo_producto):
        for item in self.__productos:
            if item.nombre == nuevo_producto.nombre:
                item.cantidad += nuevo_producto.cantidad

                print(f"> El producto '{nuevo_producto.nombre}' ya existe, se sumó la cantidad...")
                print()
                
                return
        self.__productos.append(nuevo_producto)

        print(f"> El producto '{nuevo_producto.nombre}' se agregó a la tienda...")
        print()

    def listar_productos(self):
        print()
        print("> Lista de productos: ")
        print()

        for item in self.__productos:
            print(item)


# Interacción con usuario
print("- Ingrese los siguientes datos del producto...")
print("> Nota: Se corta la carga de datos con Nombre = 0")
print()


tienda1 = Tienda()

nombre = input("Nombre: ")
while nombre != "0":
    categoria = input("Categoría: ")
    precio = float(input("Precio: $"))
    cantidad = int(input("Cantidad: "))

    producto1= Producto()
    producto1.nombre = nombre
    producto1.categoria = categoria
    producto1.precio = precio
    producto1.cantidad = cantidad

    tienda1.agregar_producto(producto1)

    print("- Ingrese los datos del siguiente producto...")

    nombre = input("Nombre: ")

tienda1.listar_productos()
