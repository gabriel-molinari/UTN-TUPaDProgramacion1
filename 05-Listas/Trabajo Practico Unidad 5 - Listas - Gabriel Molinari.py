#Trabajo Practico Unidad 5 - Listas - Gabriel Molinari

#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

"""
import random

notas = []
suma = 0

for i in range(10):
    notas.append(random.randint(1,10))

print("Lista completa de notas:")
for nota in notas:
    print(nota)

for nota in notas:
    suma += nota
promedio = suma / len(notas)
print(f"\nPromedio de notas: {promedio: .2f}")

nota_max = notas[0]
nota_min = notas[0]

for nota in notas:
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota

print(f"Nota mas alta: {nota_max}")
print(f"Nota mas baja: {nota_min}")   

"""
#--------------------------------------------------------------------------------

#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

"""
productos = []

for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

productos_ordenados = sorted(productos)

print ("\nLista de productos ordenada alfabeticamente: ")
for prod in productos_ordenados:
    print(prod)

eliminar = input("\nIngrese el producto que desea eliminar: ")

if eliminar in productos:
    productos.remove(eliminar)
    print("\nLista actualizada: ")
    for prod in productos:
        print(prod)
else:
    print(f"\nEl producto '{eliminar}' no esta en la lista.")

"""
#--------------------------------------------------------------------------------
#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

"""
import random

pares = []
impares = []

numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista completa de numeros:")
for num in numeros:
    print(num)

print("\nLista de numeros pares:")
for num in pares:
    print(num)

print("\nLista de numeros impares:")
for num in impares:
    print(num)

print(f"\nCantidad de numeros pares: {len(pares)}")
print(f"\nCantidad de numeros impares: {len(impares)}")

"""
#--------------------------------------------------------------------------------

#4) Dada una lista con valores repetidos:

#datos = [1,3,5,3,7,1,9,5,3]

#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

"""
datos = [1,3,5,3,7,1,9,5,3]

sin_repetidos = []

for valor in datos:
    if valor not in sin_repetidos:
        sin_repetidos.append(valor)

print("Lista sin elementos repetidos:")
for valor in sin_repetidos:
    print(valor)

"""

#--------------------------------------------------------------------------------

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

"""
estudiantes = []

for i in range(8):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    estudiantes.append(nombre)

accion = input("\n¿Desea agregar un nuevo estudiante (Escriba A) o elimnar uno existente (Escriba E)? ").strip().upper()

if accion == "A":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == "E":
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print(f"El estudiante '{eliminar}' no esta en la lista.")
else: 
    print("Opcion no valida.")

print("\nLista final de estudiantes: ")
for nombre in estudiantes:
    print(nombre)
"""

#--------------------------------------------------------------------------------

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

"""
lista = [10, 20, 30, 40, 50, 60, 70]

ultimo = lista[-1]

for i in range(len(lista)-1, 0, -1):
    lista[i] = lista[i-1]

lista[0] = ultimo

print("Lista rotada:")
for elem in lista:
    print(elem, end=" ")

"""

#--------------------------------------------------------------------------------

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica

"""
temperaturas = [
    [12, 22],  # Dia 1
    [14, 25],  # Dia 2
    [10, 20],  # Dia 3
    [13, 27],  # Dia 4
    [11, 21],  # Dia 5
    [15, 28],  # Dia 6
    [9, 19]    # Dia 7
]

suma_min = 0
suma_max = 0
mayor_amplitud = -1
dia_mayor_amplitud = -1


for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    
    suma_min += minima
    suma_max += maxima
    
    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print("Temperaturas de la semana (min - max):")
for i in range(len(temperaturas)):
    print(f"Día {i+1}: {temperaturas[i][0]}°C - {temperaturas[i][1]}°C")

print("\nPromedio de minimas:", promedio_min)
print("Promedio de maximas:", promedio_max)
print("Dia con mayor amplitud termica:", dia_mayor_amplitud, 
      f"(Amplitud = {mayor_amplitud}°C)")
"""

#--------------------------------------------------------------------------------
#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.

"""

notas = [
    [7, 8, 6],   # Estudiante 1
    [5, 9, 7],   # Estudiante 2
    [8, 6, 9],   # Estudiante 3
    [4, 7, 5],   # Estudiante 4
    [9, 8, 10]   # Estudiante 5
]

print("Promedio de cada estudiante:")
for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma += notas[i][j]
    promedio = suma / len(notas[i])
    print(f"Estudiante {i+1}: {promedio:.2f}")

print("\nPromedio de cada materia:")
num_estudiantes = len(notas)
num_materias = len(notas[0])

for j in range(num_materias):
    suma = 0
    for i in range(num_estudiantes):
        suma += notas[i][j]
    promedio = suma / num_estudiantes
    print(f"Materia {j+1}: {promedio:.2f}")

"""

#--------------------------------------------------------------------------------

#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

"""

tablero = [["-" for _ in range(3)] for _ in range(3)]

for fila in tablero:
    for casilla in fila:
        print(casilla, end=" ")
    print()
print()

turno = 0

while turno < 9:
    if turno % 2 == 0:
        simbolo = "X"
    else:
        simbolo = "O"
    while True:
        fila = int(input("Ingrese fila (0-2): "))
        col = int(input("Ingrese columna (0-2): "))
        if fila < 0 or fila > 2 or col < 0 or col > 2:
            print("Posicion invalida, intente de nuevo")
            continue
        if tablero[fila][col] != "-":
            print("Casilla ocupada, intente de nuevo")
            continue
        tablero[fila][col] = simbolo
        break
    for f in tablero:
        for c in f:
            print(c, end=" ")
        print()
    print()
    turno += 1

"""

#--------------------------------------------------------------------------------

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 3, 4, 6, 2, 7, 5],
    [2, 6, 3, 5, 4, 6, 3],
    [4, 5, 6, 3, 7, 2, 4],
    [3, 4, 5, 2, 6, 5, 7]
]

print("Total por producto:")
for i in range(len(ventas)):
    total = 0
    for j in range(len(ventas[i])):
        total += ventas[i][j]
    print("Producto", i+1, ":", total)

mayor_dia = -1
mayor_total = -1
for j in range(len(ventas[0])):
    suma = 0
    for i in range(len(ventas)):
        suma += ventas[i][j]
    if suma > mayor_total:
        mayor_total = suma
        mayor_dia = j+1

print("Dia con mayores ventas totales:", mayor_dia)

producto_mas = -1
ventas_mas = -1
for i in range(len(ventas)):
    suma = 0
    for j in range(len(ventas[i])):
        suma += ventas[i][j]
    if suma > ventas_mas:
        ventas_mas = suma
        producto_mas = i+1

print("Producto mas vendido en la semana:", producto_mas)

