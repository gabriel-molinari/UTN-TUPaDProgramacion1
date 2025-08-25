#Trabajo Practico 1 - Secuenciales - Gabriel Molinari

#--------------------------------------------------------------------------------
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

#print("Hola Mundo!")

#--------------------------------------------------------------------------------
#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla. 

#nombre = input("Ingrese su nombre por favor: ")
#print(f"Hola {nombre}!")

#--------------------------------------------------------------------------------

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

#nombre = input("Ingrese su nombre por favor: ")
#apellido = input("Ingrese su apellido por favor: ")
#edad = input("Ingrese su edad por favor: ")
#lugar = input("Ingrese su lugar de residencia por favor: ")

#print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

#--------------------------------------------------------------------------------

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro

#import math

#radio = float(input("Ingrese el radio del círculo: "))

#area = math.pi * radio ** 2
#perimetro = 2 * math.pi * radio

#print(f"Área del círculo: {area:.2f}")
#print(f"Perímetro del círculo: {perimetro:.2f}")

#--------------------------------------------------------------------------------

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale

""" segundos = int(input("Ingrese una cantidad de segundos: "))

horas = segundos / 1800

print(f"{segundos} segundos equivalen a {horas:.0f} hora/s") """


#--------------------------------------------------------------------------------

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

""" numero = int(input("Ingrese un numero por favor: "))

print(f"\nTabla de multiplicar del numero {numero}:\n")

for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}") """
    
#--------------------------------------------------------------------------------

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.


""" num1 = int(input("Ingrese el primer numero (distinto de 0): "))
num2 = int(input("Ingrese el segundo numero (distinto de 0): "))

if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
  
    print(f"\nResultados:")
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} × {num2} = {multiplicacion}")
    print(f"División: {num1} ÷ {num2} = {division:.2f}")
else:
    print("Error: ambos numeros deben ser distintos de 0.") """

#--------------------------------------------------------------------------------

""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:

IMC = peso en kg
    ----------------
     (altura en m)² 
"""

""" peso = float(input("Ingrese su peso en (kg): "))
altura = float(input("Ingrese su altura en metros: "))

if altura > 100:
    print("La altura tiene que ser en metros (Ejemplo 1.80)")
    exit()

if peso > 0 and altura > 0:
    imc = peso / (altura ** 2)
    print(f"\nSu Indice de Masa Corporal (IMC) es: {imc:.2f}")
else:
    print("Error: tanto el peso como la altura deben ser mayores a 0.") """

#--------------------------------------------------------------------------------

""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32 """

""" celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print(f"\nLa temperatura en Fahrenheit es: {fahrenheit:.2f}°F") """

#--------------------------------------------------------------------------------
""" 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números. """

""" num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"\nEl promedio de los tres numeros es: {promedio:.2f}") """

