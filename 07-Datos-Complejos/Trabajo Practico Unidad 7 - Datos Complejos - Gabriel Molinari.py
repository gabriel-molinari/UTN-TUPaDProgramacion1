#Trabajo Practico Unidad 7 - Datos Complejos - Gabriel Molinari

#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario actualizado:")
print(precios_frutas)
"""

#--------------------------------------------------------------------------------

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\nDiccionario con precios actualizados:")
print(precios_frutas)
"""

#--------------------------------------------------------------------------------

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

"""
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

lista_frutas = list(precios_frutas.keys())

print("\nLista de frutas:")
print(lista_frutas)
"""

#--------------------------------------------------------------------------------

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

"""
agenda = {}

print("\nIngrese 5 contactos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    agenda[nombre] = numero

nombre_buscar = input("\nIngrese el nombre del contacto a buscar: ")
if nombre_buscar in agenda:
    print(f"El número de {nombre_buscar} es: {agenda[nombre_buscar]}")
else:
    print("El contacto no existe en la agenda")
"""

#--------------------------------------------------------------------------------

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

"""
frecuencia_palabras = {}

frase = input("\nIngrese una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print("\nPalabras únicas:")
print(palabras_unicas)
print("\nFrecuencia de palabras:")
print(frecuencia_palabras)
"""

#--------------------------------------------------------------------------------

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno

"""
alumnos = {}

for i in range(3):
    nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))    
    
    alumnos[nombre] = (nota1, nota2, nota3)

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
"""

#--------------------------------------------------------------------------------

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

"""
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 5, 6, 7}

aprobaron_ambos = parcial1 & parcial2
print("\nEstudiantes que aprobaron ambos parciales:")
print(aprobaron_ambos)

aprobaron_uno = parcial1 ^ parcial2
print("\nEstudiantes que aprobaron solo un parcial:")
print(aprobaron_uno)

aprobaron_alguno = parcial1 | parcial2
print("\nEstudiantes que aprobaron al menos un parcial:")
print(aprobaron_alguno)
"""

#--------------------------------------------------------------------------------

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

"""
inventario = {'Arroz': 100, 'Fideos': 150, 'Aceite': 80}

while True:
    print("\n1. Consultar stock")
    print("2. Agregar unidades a producto existente")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    
    opcion = input("\nSeleccione una opción (1-4): ")
    
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        if producto in inventario:
            print(f"Stock de {producto}: {inventario[producto]} unidades")
        else:
            print("El producto no existe en el inventario")
            
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        if producto in inventario:
            unidades = int(input("Ingrese cantidad a agregar: "))
            inventario[producto] += unidades
            print(f"Stock actualizado de {producto}: {inventario[producto]} unidades")
        else:
            print("El producto no existe en el inventario")
            
    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in inventario:
            stock = int(input("Ingrese el stock inicial: "))
            inventario[producto] = stock
            print(f"Producto {producto} agregado con stock inicial de {stock} unidades")
        else:
            print("El producto ya existe en el inventario")
            
    elif opcion == "4":
        break
    
    else:
        print("Opción inválida")

print("\nInventario final:")
print(inventario)
"""

#--------------------------------------------------------------------------------

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora

"""
agenda = {
    ('lunes', '09:00'): 'Reunión de trabajo',
    ('martes', '15:30'): 'Clase de programación',
    ('miércoles', '11:00'): 'Consulta médica',
    ('viernes', '18:00'): 'Gimnasio'
}

dia = input("\nIngrese el día (ej: lunes): ").lower()
hora = input("Ingrese la hora (formato HH:MM): ")

momento = (dia, hora)

if momento in agenda:
    print(f"\nActividad programada: {agenda[momento]}")
else:
    print("\nNo hay actividades programadas para ese dia y hora")
"""

#--------------------------------------------------------------------------------

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores

paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción'
}

capitales = {capital: pais for pais, capital in paises.items()}

print("\nDiccionario original (país: capital):")
print(paises)
print("\nDiccionario invertido (capital: país):")
print(capitales)

