#Trabajo Practico Unidad 6 - Funciones - Gabriel Molinari

#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

"""
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

"""

#--------------------------------------------------------------------------------

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
#Llamar a esta función desde el programa principal solicitando el nombre al usuario.

"""
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)
"""

#--------------------------------------------------------------------------------

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar 
#a esta función con los valores ingresados.

"""
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
"""

#--------------------------------------------------------------------------------

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

"""
def calcular_area_circulo(radio):
    PI = 3.14159
    return PI * (radio ** 2)

def calcular_perimetro_circulo(radio):
    PI = 3.14159
    return 2 * PI * radio

radio_usuario = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio_usuario)
perimetro = calcular_perimetro_circulo(radio_usuario)

print(f"Para un círculo de radio {radio_usuario}:")
print(f"El área es: {area:.2f}")
print(f"El perímetro es: {perimetro:.2f}")
"""

#--------------------------------------------------------------------------------

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

"""
def segundos_a_horas(segundos):
    return segundos / 3600

segundos_usuario = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos_usuario)
print(f"{segundos_usuario} segundos equivalen a {horas:.2f} horas")
"""

#--------------------------------------------------------------------------------

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

"""
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero_usuario = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_usuario)
"""

#--------------------------------------------------------------------------------

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

"""
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(numero1, numero2)

print("\nResultados de las operaciones:")
print(f"Suma: {numero1} + {numero2} = {resultados[0]}")
print(f"Resta: {numero1} - {numero2} = {resultados[1]}")
print(f"Multiplicación: {numero1} * {numero2} = {resultados[2]}")
print(f"División: {numero1} / {numero2} = {resultados[3]}")
"""

#--------------------------------------------------------------------------------

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

"""
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso_usuario = float(input("Ingrese su peso en kilogramos: "))
altura_usuario = float(input("Ingrese su altura en metros (Ej 1.75): "))

imc = calcular_imc(peso_usuario, altura_usuario)
print(f"\nSu Índice de Masa Corporal (IMC) es: {imc:.2f}")
"""

#--------------------------------------------------------------------------------

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

"""
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"\n{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F")
"""

#--------------------------------------------------------------------------------

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"\nEl promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

