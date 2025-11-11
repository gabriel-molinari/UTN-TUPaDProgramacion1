#TP Integrador Programacion - Gabriel Molinari - Fecha de entrega: 11/11/2025

#------------IMPORTS------------#
import os
import unicodedata

#------------CONSTANTES------------#
nombre_archivo_csv = "datos_paises.csv"

#CONSTANTES DE INDICES PARA LA LECTURA DEL CSV
#ASUMIENDO EL ORDEN: NOMBRE, POBLACION, SUPERFICIE, CONTINENTE
indice_nombre = 0
indice_poblacion = 1
indice_superficie = 2
indice_continente = 3

#------------FUNCIONES------------#

#FUNCION PARA NORMALIZAR TEXTO -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def normalizar(texto):

    #CONVIERTE A MINÚSCULA Y ELIMINA ACENTOS
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

#FUNCION PARA CARGAR EL ARCHIVO CSV --------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_datos_csv(nombre_archivo):

    #SE LEEN LOS DATOS DESDE EL ARCHIVO CSV Y LOS ALMACENA EN UNA LISTA DE DICCIONARIOS.
    #REALIZA LA CONVERSIÓN DE TIPOS PARA POBLACIÓN Y SUPERFICIE.

    paises = []
    try:
        # ABRIR EL ARCHIVO PARA LECTURA
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # SALTAR LA CABECERA (PRIMERA LÍNEA)
            next(archivo)
            
            for linea in archivo:
                # DIVIDIR LA LÍNEA POR COMAS (FORMATO CSV)
                campos = linea.strip().split(',')
                
                # CONTROLAR ERRORES DE FORMATO BÁSICOS (QUE HAYA 4 CAMPOS)
                if len(campos) == 4:
                    try:
                        pais = {
                        'nombre': campos[indice_nombre].strip(),
                        'poblacion': int(campos[indice_poblacion]),
                        'superficie': int(campos[indice_superficie]),
                        'continente': campos[indice_continente].strip()
                        }
                        
                        paises.append(pais)
                    except ValueError:
                        print(f"ERROR: VALOR INVÁLIDO EN POBLACIÓN O SUPERFICIE EN LA LÍNEA: {linea.strip()}")
                        continue
        
        print(f"ÉXITO: SE CARGARON {len(paises)} PAÍSES.")
        return paises
    
    except FileNotFoundError:
        print(f"ERROR: EL ARCHIVO {nombre_archivo} NO FUE ENCONTRADO.")
        return []
    except Exception as e:
        print(f"ERROR INESPERADO AL LEER EL ARCHIVO: {e}")
        return []

#FUNCION PARA MOSTRAR LOS PAISES -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mostrar_paises(paises_lista):
   
    #MUESTRA LOS DATOS DE LA LISTA DE PAÍSES FORMATEADOS.
    
    if not paises_lista:
        print("NO HAY PAÍSES PARA MOSTRAR.")
        return

    print("\n--- LISTADO DE PAÍSES ---")
    for pais in paises_lista:
        print(f"NOMBRE: {pais['nombre']:<20} | CONTINENTE: {pais['continente']:<10} | POBLACIÓN: {pais['poblacion']:>15,} | SUPERFICIE: {pais['superficie']:>10,} km²")
    print("--------------------------\n")

#FUNCION PARA BUSCAR PAIS POR NOMBRE -------------------------------------------------------------------------------------------------------------------------------------------------------------------
def buscar_pais_por_nombre(paises_lista):
    
    #BUSCA PAÍSES POR COINCIDENCIA PARCIAL O EXACTA DEL NOMBRE.
   
    if not paises_lista:
        print("LOS DATOS NO HAN SIDO CARGADOS AÚN.")
        return

    termino = input("INGRESE EL NOMBRE O PARTE DEL NOMBRE DEL PAÍS A BUSCAR: ").strip().lower()
    resultado = []
    
    for pais in paises_lista:
        # LÓGICA CONDICIONAL PARA COINCIDENCIA PARCIAL
        if termino in pais['nombre'].lower():
            resultado.append(pais)
    
    if resultado:
        print(f"\nSE ENCONTRARON {len(resultado)} PAÍSES CON '{termino}':")
        mostrar_paises(resultado)
    else:
        # MENSAJE CLARO DE NO RESULTADO
        print(f"NO SE ENCONTRARON PAÍSES QUE COINCIDAN CON '{termino}'.")

#FUNCION PARA FILTRAR POR CONTINENTE -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def filtrar_por_continente(paises_lista):
    
    #FILTRA PAÍSES BASADO EN EL CONTINENTE ESPECIFICADO.
    
    if not paises_lista:
        print("LOS DATOS NO HAN SIDO CARGADOS AÚN.")
        return

    continente_filtro = input("INGRESE EL NOMBRE DEL CONTINENTE (EJ: AMÉRICA, ASIA): ").strip().lower()
    resultado = []
    
    for pais in paises_lista: # ESTRUCTURA REPETITIVA
        # LÓGICA CONDICIONAL
        if normalizar(pais['continente']) == continente_filtro:
            resultado.append(pais)
    
    if resultado:
        print(f"\nPAÍSES FILTRADOS EN {continente_filtro.upper()}:")
        mostrar_paises(resultado)
    else:
        print(f"NO SE ENCONTRARON PAÍSES EN EL CONTINENTE '{continente_filtro}'.")

#FUNCION PARA OBTENER UN RANGO VÁLIDO ------------------------------------------------------------------------------------------------------------------------------------------------------------------

def obtener_rango_valido(propiedad):
    
    #FUNCIÓN AUXILIAR PARA OBTENER RANGOS NUMÉRICOS Y VALIDAR ENTRADAS.
   
    try:
        minimo = int(input(f"INGRESE EL MÍNIMO DE {propiedad}: "))
        maximo = int(input(f"INGRESE EL MÁXIMO DE {propiedad}: "))
        # LÓGICA CONDICIONAL: VALIDACIÓN DE RANGO
        if minimo > maximo:
            print("ADVERTENCIA: EL MÍNIMO ES MAYOR QUE EL MÁXIMO. REINTENTE.")
            return None, None
        if minimo < 0 or maximo < 0:
            print("LOS VALORES DEBEN SER POSITIVOS.")
            return None, None
        return minimo, maximo
    except ValueError:
        print("ERROR: INGRESE UN VALOR NUMÉRICO ENTERO VÁLIDO.")
        return None, None

#FUNCION PARA FILTRAR POR RANGO DE POBLACIÓN -----------------------------------------------------------------------------------------------------------------------------------------------------------

def filtrar_por_rango_poblacion(paises_lista):
    
    #FILTRA PAÍSES POR RANGO DE POBLACIÓN.
    
    if not paises_lista:
        print("LOS DATOS NO HAN SIDO CARGADOS AÚN.")
        return

    min_pop, max_pop = obtener_rango_valido("POBLACIÓN")
    
    if min_pop is None:
        return

    resultado = []
    for pais in paises_lista: # ESTRUCTURA REPETITIVA
        # LÓGICA CONDICIONAL DE RANGO
        if min_pop <= pais['poblacion'] <= max_pop:
            resultado.append(pais)
    
    if resultado:
        print(f"\nPAÍSES CON POBLACIÓN ENTRE {min_pop:,} Y {max_pop:,}:")
        mostrar_paises(resultado)
    else:
        print("NO SE ENCONTRARON PAÍSES EN ESE RANGO DE POBLACIÓN.")

#FUNCION PARA FILTRAR POR RANGO DE SUPERFICIE ----------------------------------------------------------------------------------------------------------------------------------------------------------
def filtrar_por_rango_superficie(paises_lista):
   
    #FILTRA PAÍSES POR RANGO DE SUPERFICIE.
   
    if not paises_lista:
        print("LOS DATOS NO HAN SIDO CARGADOS AÚN.")
        return

    min_sup, max_sup = obtener_rango_valido("SUPERFICIE")
    
    if min_sup is None:
        return

    resultado = []
    for pais in paises_lista: # ESTRUCTURA REPETITIVA
        # LÓGICA CONDICIONAL DE RANGO
        if min_sup <= pais['superficie'] <= max_sup:
            resultado.append(pais)
    
    if resultado:
        print(f"\nPAÍSES CON SUPERFICIE ENTRE {min_sup:,} Y {max_sup:,} KM²:")
        mostrar_paises(resultado)
    else:
        print("NO SE ENCONTRARON PAÍSES EN ESE RANGO DE SUPERFICIE.")

#FUNCION PARA ORDENAR paises ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ordenar_paises(paises_lista):
   
    #PERMITE ORDENAR LA LISTA DE PAÍSES POR NOMBRE, POBLACIÓN O SUPERFICIE.
   
    if not paises_lista:
        print("LOS DATOS NO HAN SIDO CARGADOS AÚN.")
        return

    print("\n--- OPCIONES DE ORDENAMIENTO ---")
    print("1. POR NOMBRE")
    print("2. POR POBLACIÓN")
    print("3. POR SUPERFICIE")
    opcion = input("SELECCIONE CRITERIO (1-3): ")

    reverso = False
    if opcion in ('2', '3'):
        orden = input("ORDEN (A: ASCENDENTE / D: DESCENDENTE): ").strip().upper()
        if orden == 'D':
            reverso = True

    # LÓGICA CONDICIONAL PARA SELECCIONAR LA CLAVE DE ORDENAMIENTO
    if opcion == '1':
        clave = 'nombre'
    elif opcion == '2':
        clave = 'poblacion'
    elif opcion == '3':
        clave = 'superficie'
    else:
        print("OPCIÓN DE ORDENAMIENTO INVÁLIDA.")
        return

    # UTILIZANDO LA FUNCIÓN DE ORDENAMIENTO DE PYTHON (MÉTODO EFICIENTE)
    # SE CREA UNA COPIA PARA NO MODIFICAR LA LISTA ORIGINAL DIRECTAMENTE
    paises_ordenados = sorted(paises_lista, key=lambda pais: pais[clave], reverse=reverso)
    
    print(f"\nLISTADO ORDENADO POR {clave.upper()}:")
    mostrar_paises(paises_ordenados)

#FUNCION PARA MOSTRAR ESTADISTICAS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_estadisticas(paises_lista):
    
    #CALCULA Y MUESTRA DIVERSAS ESTADÍSTICAS BÁSICAS.
    
    if not paises_lista:
        print("LOS DATOS NO HAN SIDO CARGADOS AÚN PARA CALCULAR ESTADÍSTICAS.")
        return

    total_paises = len(paises_lista)
    total_poblacion = 0
    total_superficie = 0 
   
    # CÁLCULO DE TOTALES USANDO ESTRUCTURA REPETITIVA
    for pais in paises_lista:
        total_poblacion += pais['poblacion']
        total_superficie += pais['superficie']

    print("\n--- ESTADÍSTICAS CLAVE ---")

    # 1. PAÍS CON MAYOR Y MENOR POBLACIÓN
    if paises_lista:
        # NOTA: USANDO MAX/MIN CON UNA FUNCIÓN CLAVE PARA ENCONTRAR DENTRO DE LA LISTA DE DICCIONARIOS
        pais_mayor_pop = max(paises_lista, key=lambda pais: pais['poblacion'])
        pais_menor_pop = min(paises_lista, key=lambda pais: pais['poblacion'])

        print(f"PAÍS CON MAYOR POBLACIÓN: {pais_mayor_pop['nombre']} ({pais_mayor_pop['poblacion']:,})")
        print(f"PAÍS CON MENOR POBLACIÓN: {pais_menor_pop['nombre']} ({pais_menor_pop['poblacion']:,})")
    
    # 2. PROMEDIO DE POBLACIÓN
    promedio_poblacion = total_poblacion / total_paises
    print(f"PROMEDIO DE POBLACIÓN: {int(promedio_poblacion):,}")

    # 3. PROMEDIO DE SUPERFICIE
    promedio_superficie = total_superficie / total_paises
    print(f"PROMEDIO DE SUPERFICIE: {int(promedio_superficie):,} KM²")

    # 4. CANTIDAD DE PAÍSES POR CONTINENTE
    conteo_continentes = {} # USO DE DICCIONARIO PARA CONTAR
    for pais in paises_lista:
        continente = pais['continente']
        # LÓGICA CONDICIONAL DE CONTEO
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1
    
    print("\nCANTIDAD DE PAÍSES POR CONTINENTE:")
    for continente, CANTIDAD in conteo_continentes.items():
        print(f"- {continente}: {CANTIDAD}")

#FUNCION DE MENU PRINCIPAL -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def menu_principal(paises):
    
    #FUNCIÓN PRINCIPAL QUE GESTIONA EL MENÚ DE OPCIONES.    
    
    while True: # ESTRUCTURA REPETITIVA
        print("\n===== GESTIÓN DE DATOS DE PAÍSES =====")        
        print("1. BUSCAR PAÍS POR NOMBRE")
        print("2. FILTRAR POR CONTINENTE")
        print("3. FILTRAR POR RANGO DE POBLACIÓN")
        print("4. FILTRAR POR RANGO DE SUPERFICIE")
        print("5. ORDENAR PAÍSES")
        print("6. MOSTRAR ESTADÍSTICAS")
        print("7. MOSTRAR TODOS LOS PAÍSES")
        print("8. SALIR")
        
        opcion = input("INGRESE SU OPCIÓN: ")
        
        # LÓGICA CONDICIONAL PARA EL MENÚ
        if opcion == '1':
            buscar_pais_por_nombre(paises)
        elif opcion == '2':
            filtrar_por_continente(paises)
        elif opcion == '3':
            filtrar_por_rango_poblacion(paises)
        elif opcion == '4':
            filtrar_por_rango_superficie(paises)
        elif opcion == '5':
            ordenar_paises(paises)
        elif opcion == '6':
            mostrar_estadisticas(paises)
        elif opcion == '7':
            mostrar_paises(paises)
        elif opcion == '8':
            print("SALIENDO DEL SISTEMA.")
            break
        else:
            print("OPCIÓN NO VÁLIDA. INTENTE DE NUEVO.")

#BLOQUE DE EJECUCIÓN PRINCIPAL -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # INTENTAR CARGAR DATOS DESDE CSV AL INICIO
    datos_paises = cargar_datos_csv(nombre_archivo_csv)
    
    if datos_paises:  # SI SE CARGARON DATOS CORRECTAMENTE
        print ("Archivo cargado con exito. El archivo se encuentra en la ruta: " + os.getcwd())
        menu_principal(datos_paises)
    else:
        print("No se pudo cargar el archivo. El programa finalizará. El archivo tiene que estar en: " + os.getcwd())