o Descripción del programa.

Este proyecto consiste en una aplicación de consola desarrollada en Python que permite gestionar información sobre países. 
El sistema lee datos desde un archivo CSV y ofrece funcionalidades de búsqueda, filtrado, ordenamiento y generación de estadísticas. 
Está diseñado para aplicar estructuras de datos como listas y diccionarios, junto con funciones, condicionales y estructuras repetitivas.


------------------------------------------------------------------------------------------------------------------------------------------------------------
o Instrucciones de uso.

1) Asegurarse de tener Python 3.x instalado.
2) Colocar el archivo datos_paises.csv en la ruta C:\Users\<NombreUsuario>
3) Ejecutar el programa
4) Navegar por el menú de opciones en consola.

------------------------------------------------------------------------------------------------------------------------------------------------------------
o Ejemplos de entradas y salidas.

1. Buscar país por nombre
Entrada:
INGRESE SU OPCIÓN: 1
INGRESE EL NOMBRE O PARTE DEL NOMBRE DEL PAÍS A BUSCAR: Argentina

Salida:
SE ENCONTRARON 1 PAÍSES CON 'argentina':

--- LISTADO DE PAÍSES ---
NOMBRE: Argentina           | CONTINENTE: América    | POBLACIÓN:      45,376,763 | SUPERFICIE:  2,780,400 km²
--------------------------

2. Filtrar por continente
Entrada:
INGRESE SU OPCIÓN: 2
INGRESE EL NOMBRE DEL CONTINENTE (EJ: AMÉRICA, ASIA): África

Salida:
PAÍSES FILTRADOS EN ÁFRICA:

--- LISTADO DE PAÍSES ---
NOMBRE: Egipto              | CONTINENTE: África     | POBLACIÓN:     110,000,000 | SUPERFICIE:  1,002,450 km²
NOMBRE: Sudáfrica           | CONTINENTE: África     | POBLACIÓN:      60,000,000 | SUPERFICIE:  1,219,090 km²
NOMBRE: Argelia             | CONTINENTE: África     | POBLACIÓN:      44,900,000 | SUPERFICIE:  2,381,741 km²
--------------------------

3. Filtrar por rango de población
Entrada:
INGRESE SU OPCIÓN: 3
INGRESE EL MÍNIMO DE POBLACIÓN: 50_000_000
INGRESE EL MÁXIMO DE POBLACIÓN: 150_000_000

Salida:
PAÍSES CON POBLACIÓN ENTRE 50,000,000 Y 150,000,000:

--- LISTADO DE PAÍSES ---
NOMBRE: México              | CONTINENTE: América    | POBLACIÓN:     126,000,000 | SUPERFICIE:  1,964,375 km²
NOMBRE: Egipto              | CONTINENTE: África     | POBLACIÓN:     110,000,000 | SUPERFICIE:  1,002,450 km²
NOMBRE: Japón               | CONTINENTE: Asia       | POBLACIÓN:     125,800,000 | SUPERFICIE:    377,975 km²
--------------------------

4. Ordenar países por superficie descendente
Entrada:
INGRESE SU OPCIÓN: 5
SELECCIONE CRITERIO (1-3): 3
ORDEN (A: ASCENDENTE / D: DESCENDENTE): D

Salida:
LISTADO ORDENADO POR SUPERFICIE:

--- LISTADO DE PAÍSES ---
NOMBRE: Brasil              | CONTINENTE: América    | POBLACIÓN:     213,993,437 | SUPERFICIE:  8,515,767 km²
NOMBRE: Canadá              | CONTINENTE: América    | POBLACIÓN:      38,900,000 | SUPERFICIE:  9,984,670 km²
NOMBRE: Australia           | CONTINENTE: Oceanía    | POBLACIÓN:      26,000,000 | SUPERFICIE:  7,692,024 km²
...
--------------------------

5. Mostrar estadísticas
Entrada:
INGRESE SU OPCIÓN: 6

--- ESTADÍSTICAS CLAVE ---
PAÍS CON MAYOR POBLACIÓN: India (1,428,600,000)
PAÍS CON MENOR POBLACIÓN: Australia (26,000,000)
PROMEDIO DE POBLACIÓN: 226,000,000
PROMEDIO DE SUPERFICIE: 3,500,000 KM²

CANTIDAD DE PAÍSES POR CONTINENTE:
- América: 4
- Europa: 1
- Asia: 2
- África: 3
- Oceanía: 1

------------------------------------------------------------------------------------------------------------------------------------------------------------
o Participación de los integrantes.

Gabriel Molinari — Desarrollo, validación, pruebas y documentación.