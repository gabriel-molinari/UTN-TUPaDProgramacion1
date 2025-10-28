#Trabajo Practico Unidad 8 - Manejo de archivos - Gabriel Molinari

#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

"""
with open("productos.txt", "w") as archivo:
    archivo.write("Manzana,120,50\n")
    archivo.write("Lechuga,80,30\n")
    archivo.write("Tomate,150,40\n")
"""

#--------------------------------------------------------------------------------

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
"""
with open("productos.txt", "r") as archivo:
    for linea in archivo:
       
        partes = linea.strip().split(",")        
        
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]        
        
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
"""
#--------------------------------------------------------------------------------

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

"""
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        nombre, precio, cantidad = partes
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("\n--- Agregar nuevo producto ---")
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("Producto agregado correctamente.")
"""

#--------------------------------------------------------------------------------

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

"""
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        nombre = partes[0]
        precio = float(partes[1])      
        cantidad = int(partes[2])   

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        productos.append(producto)

print(productos)
"""

#--------------------------------------------------------------------------------

#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

"""
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        nombre = partes[0]
        precio = float(partes[1])
        cantidad = int(partes[2])
        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })

buscado = input("Ingrese el nombre del producto a buscar: ")

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == buscado.lower():
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("El producto no existe en la lista.")
"""

#--------------------------------------------------------------------------------

#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

#Invento datos para guardar
productos = [
    {"nombre": "Manzana", "precio": 120.0, "cantidad": 50},
    {"nombre": "Lechuga", "precio": 80.0, "cantidad": 30},
    {"nombre": "Tomate", "precio": 150.0, "cantidad": 40}
]

with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)

print("Archivo productos.txt actualizado correctamente.")

with open("productos.txt", "r") as archivo:
    print(archivo.read())



