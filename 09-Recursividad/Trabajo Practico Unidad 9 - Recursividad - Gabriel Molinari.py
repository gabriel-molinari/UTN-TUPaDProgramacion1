#Trabajo Practico Unidad 9 - Recursividad - Gabriel Molinari

#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

"""
def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:        
        return n * factorial(n - 1)

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")
"""

#--------------------------------------------------------------------------------

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

"""
def fibonacci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese hasta qué posición de la serie de Fibonacci quiere ver: "))

print(f"Serie de Fibonacci hasta la posición {pos}:")
for i in range(pos + 1):
    print(fibonacci(i))
"""

#--------------------------------------------------------------------------------

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
#algoritmo general

"""
def potencia(base, exponente):
    
    if exponente == 0:
        return 1
    else:       
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")
"""

#--------------------------------------------------------------------------------

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.
#
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
#unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
#procedimiento:
#1. Dividir el número por 2.
#2. Guardar el resto (0 o 1).
#3. Repetir el proceso con el cociente hasta que llegue a 0.
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
#
#Convertir el número 10 a binario:
#10 ÷ 2 = 5 resto: 0
#5 ÷ 2 = 2 resto: 1
#2 ÷ 2 = 1 resto: 0
#1 ÷ 2 = 0 resto: 1
#Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010"

"""
def decimal_a_binario(n):
    
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:        
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número entero positivo: "))
print(f"El número {num} en binario es: {decimal_a_binario(num)}")
"""

#--------------------------------------------------------------------------------

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

"""
def es_palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])

print(es_palindromo("reconocer"))
print(es_palindromo("radar"))
print(es_palindromo("python"))
"""

#--------------------------------------------------------------------------------

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

"""
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1234))  # 10
print(suma_digitos(9))     # 9
print(suma_digitos(305))   # 8
"""

#--------------------------------------------------------------------------------

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.
#Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)

"""
def contar_bloques(n):

    if n == 1:
        return 1
    else:       
        return n + contar_bloques(n - 1)

print(contar_bloques(1))
print(contar_bloques(2))
print(contar_bloques(4))
"""

#--------------------------------------------------------------------------------

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.
#Ejemplos:
#contar_digito(12233421, 2) → 3
#contar_digito(5555, 5) → 4
#contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    
    if numero == 0:
        return 0
    else:        
        ultimo = numero % 10

        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar (0-9): "))

resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")


