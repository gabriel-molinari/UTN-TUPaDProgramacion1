#Trabajo Practico Unidad 4 - Estructuras Repetitivas - Gabriel Molinari

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

"""
for i in range(101):
    print(i)
"""

#--------------------------------------------------------------------------------

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

"""
numero = input("Ingrese un numero entero: ")

digitos = 0

try:   ##PRUEBO DE USAR TRY POR SI EL VALOR ES VACIO O TEXTO
    numero = int(numero)

    while numero > 0:
     numero //= 10  #ELIMINO EL ULTIMO DIGITO
     digitos += 1

    #SI SOLO HAY 1 DIGITO
    if digitos == 0:
       digitos = 1

    print("El numero tiene", digitos, "digitos.")

except ValueError:
    print("No es un numero entero.")

"""
#--------------------------------------------------------------------------------

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

"""
suma = 0
numero1 = int(input("Ingrese el valor minimo: "))
numero2 = int(input("Ingrese el valor maximo: "))

for i in range(numero1 + 1, numero2):
    suma += i

print("La suma final es: ", suma)

"""

#--------------------------------------------------------------------------------

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

"""
numero = 1
suma = 0

while numero != 0:
    entero = int(input("Ingrese un numero entero: "))

    if (entero == 0):
        break

    suma += entero

print("La suma total de los valores es: ", suma)

"""

#--------------------------------------------------------------------------------
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

"""
import random
numero_secreto = random.randint(0, 9)

intentos = 0
adivinanza = -1

print("Ingrese un numero del 0 al 9 para intentar adivinarlo")

while adivinanza != numero_secreto:
    try:
        adivinanza = int(input("Tu intento: "))
        intentos += 1

        if adivinanza < 0 or adivinanza > 9:
            print("El numero debe estar entre 0 y 9.")
        elif adivinanza != numero_secreto:
            print("Incorrecto. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un numero entero del 0 al 9.")

print("Correcto,  el numero era", numero_secreto)
print("Cantidad de intentos", intentos, "intento/s.")

"""

#--------------------------------------------------------------------------------
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

"""
for i in range (100, -1, -2):
    print(i)
"""

#--------------------------------------------------------------------------------
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

"""
suma = 0

try:
    numero = int(input("Ingrese un numero entero positivo: "))

    for i in range(0, numero):  #NO TOMO EN CUENTA EL NUMERO INGRESADO PARA LA SUMA
        suma += i

    print ("La suma total del rango es: ", suma)

except ValueError:
        print("Error, no ingreso un numero entero positivo")

"""

#--------------------------------------------------------------------------------
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

"""
cantidad = 5   #CAMBIAR POR 100
pares = 0
impares = 0
positivos = 0
negativos = 0
neutro = 0

print(f"Ingrese {cantidad} numeros enteros:")

for i in range(cantidad):
    while True:
        try:
            numero = int(input(f"Numero {i+1}: "))
            break
        except ValueError:
            print("Error, por favor ingrese un numero entero.")
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutro += 1   #POR SI ES 0

print("\nResultados:")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")
print(f"Numeros neutro: {neutro}")

"""

#--------------------------------------------------------------------------------
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

"""
cantidad = 5 #CAMBIAR POR 100
suma_total = 0
media = 0

print(f"Ingresa {cantidad} numeros enteros:")

for i in range(1, cantidad + 1):
    while True:
        try:
            numero = int(input(f"Numero {i}: "))
            suma_total += numero
            break
        except ValueError:
            print("Error, por favor ingrese un numero entero.")

media = suma_total / cantidad

print("\nResultado:")
print(f"La media de los {cantidad} numeros ingresados es: {media}")

"""

#--------------------------------------------------------------------------------
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

"""
invertido = ""
numero = input("Ingrese un numero entero: ")

#VALIDO SI ES NEGATIVO
es_negativo = numero.startswith('-')

#LE ELIMINO EL SIGNO
if es_negativo:
    numero = numero[1:]

for digito in numero:
    invertido = digito + invertido  #INVIERTE EL NUMERO

#SE LE VUELVE A AGREGAR EL SIGNO NEGATIVO SI CORRESPONDE
if es_negativo:
    invertido = '-' + invertido

print("Numero invertido:", invertido)

"""