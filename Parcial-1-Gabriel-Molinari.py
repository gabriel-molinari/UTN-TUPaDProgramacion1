#Parcial 1 Programacion - Gabriel Molinari

#----DECLARACION DE VARIABLES----#
lista_titulos = ["El Señor de los Anillos", "Romeo y Julieta", "Orgullo y Prejuicio", "Matar un Ruiseñor","Cumbres borrascosas"]   #COLOCO LOS EJEMPLOS PARA QUE NO EMPIECE VACIA LA LISTA
lista_cant_ejemplares = [5,0,3,7,0]
opcion = 0
opcion_valida = False

#----BLOQUE PRINCIPAL----#
while (opcion != 8):
    
    #----MENU PRINCIPAL----#
    print("\n")
    print("****Menú Principal****")
    print("Elija una opción (Coloque numero y presione enter)")
    print("[1] || Ingresar títulos")
    print("[2] || Ingresar ejemplares")
    print("[3] || Mostrar catálogo")
    print("[4] || Consultar disponibilidad")
    print("[5] || Listar agotados")
    print("[6] || Agregar título")
    print("[7] || Actualizar ejemplares (préstamo/devolución) ")
    print("[8] || Salir")
    print("\n")
    
    #----VALIDO LA OPCION ELEGIDA----#
    while not opcion_valida:
        opcion_input = input("Opción: ")
        if opcion_input.isdigit():
            opcion = int(opcion_input)
            if 1 <= opcion <= 8:
                opcion_valida = True
            else:
                print("\nOpción inválida. Debe ingresar un número del 1 al 8.")
        else:
            print("\nOpción inválida. Debe ingresar un número del 1 al 8.")
    
    #----CASE CON OPCION ELEGIDA----#
    if (opcion == 1):     #Ingresar títulos------------------------------------------------------------------------------------------------
        
        #PIDO LA CANTIDAD DE TITULOS NUEVOS A INGRESAR
        cantidad_titulos = -1
        while cantidad_titulos < 1:
            cantidad_input = input("Ingrese la cantidad de títulos nuevos que quiere ingresar: ")
            if cantidad_input.isdigit():
                cantidad_titulos = int(cantidad_input)
                if cantidad_titulos < 1:
                    print("La cantidad debe ser un número entero positivo.")
            else:
                print("La cantidad debe ser un número entero positivo.")
        for i in range(cantidad_titulos):

            titulo = ""

            #PIDO EL NOMBRE DEL NUEVO TITULO
            while titulo.strip() == "":
                titulo = input("Ingrese el nombre del nuevo título: ").strip()
                if titulo == "":
                    print("El título no puede estar vacío. Intente nuevamente.")
            
            # VALIDO QUE NO EXISTA YA ESE TITULO
            if titulo in lista_titulos:
                print("Ese título ya existe en el catálogo. No se agrega.")
            else:
                lista_titulos.append(titulo)
                lista_cant_ejemplares.append(0)  # SIN EJEMPLARES AL INICIO

        print("\nNuevo/s libro/s ingresado/s")
    
    elif (opcion == 2):   #Ingresar ejemplares---------------------------------------------------------------------------------------------
    
        #MUESTRO LOS LIBROS DISPONIBLES PARA ELEGIR
        print("Lista de libros disponibles:\n")
        for i, titulo in enumerate(lista_titulos):
            print(f"{i+1}. {titulo} (Cantidad de ejemplares actuales: {lista_cant_ejemplares[i]})")
    
        titulo = -1
        while titulo < 1 or titulo > len(lista_titulos):
            titulo_input = input("\nIngrese el número del libro que desea elegir: ")
            if titulo_input.isdigit():
                titulo = int(titulo_input)
                if titulo < 1 or titulo > len(lista_titulos):
                    print("Opción no válida. Ingrese un número de libro válido.")
            else:
                print("Opción no válida. Ingrese un número de libro válido.")
    
        # VALIDO QUE SEA LA OPCION CORRECTA
        if 1 <= titulo <= len(lista_titulos):
            cant_ejemplares = -1
            while cant_ejemplares < 0:
                cant_input = input("\nIngrese la cantidad de ejemplares a agregar: ")
                if cant_input.isdigit():
                    cant_ejemplares = int(cant_input)
                    if cant_ejemplares < 0:
                        print("La cantidad debe ser un número entero positivo o cero.")
                else:
                    print("La cantidad debe ser un número entero positivo o cero.")
            lista_cant_ejemplares[titulo-1] += cant_ejemplares
            print("\nCantidad actualizada")
        else:
            print("\nOpción no válida")

    elif (opcion == 3):   #Mostrar catálogo------------------------------------------------------------------------------------------------

        #MOSTRAR LOS LIBROS Y SUS CANTIDADES
        print("\nLibros disponibles:")
        print(f"{'\nN°':<4}{'Título':<40}{'Cantidad de ejemplares'}")
        for i, titulo in enumerate(lista_titulos):
            print(f"{i+1:<4}{titulo:<40}{lista_cant_ejemplares[i]}")
    
    elif (opcion == 4):   #Consultar disponibilidad----------------------------------------------------------------------------------------

        #MUESTRO LOS LIBROS DISPONIBLES PARA ELEGIR
        print("Lista de libros para consultar ejemplares:\n")
        for i, titulo in enumerate(lista_titulos):
            print(f"{i+1}. {titulo}")
    
        while True:
            titulo_input = input("\nIngrese el número del libro que desea elegir: ")
            if titulo_input.isdigit():
                titulo = int(titulo_input)
                if 1 <= titulo <= len(lista_titulos):
                    print(f"\nCantidad de ejemplares disponibles:  {lista_cant_ejemplares[titulo-1]}")
                    break
                else:
                    print("Opción no válida. Ingrese un número de libro válido.")
            else:
                print("Opción no válida. Ingrese un número de libro válido.")
        else:
            print("\n Opción no válida")    
    
    elif (opcion == 5):   #Listar agotados-------------------------------------------------------------------------------------------------

        #MUESTRO LOS LIBROS AGOTADOS
        print("Lista de libros agotados:\n")

        for i, titulo in enumerate(lista_titulos):
            if lista_cant_ejemplares[i] == 0:
                print(f"{i+1}. {titulo}")

    elif (opcion == 6):   #Agregar título--------------------------------------------------------------------------------------------------
        
        #PIDO EL NOMBRE Y CANTIDAD DEL NUEVO TITULO
        titulo = ""
        while titulo.strip() == "":
            titulo = input("Ingrese el nombre del nuevo título: ").strip()
            if titulo == "":
                print("El título no puede estar vacío. Intente nuevamente.")
        if titulo in lista_titulos:
            print("Ese título ya existe en el catálogo. No se agrega.")
        else:
            cant_ejemplares = -1
            while cant_ejemplares < 0:
                cant_input = input("Ingrese la cantidad de ejemplares del nuevo título: ")
                if cant_input.isdigit():
                    cant_ejemplares = int(cant_input)
                    if cant_ejemplares < 0:
                        print("La cantidad debe ser un número entero positivo o cero.")
                else:
                    print("La cantidad debe ser un número entero positivo o cero.")
            lista_titulos.append(titulo)
            lista_cant_ejemplares.append(cant_ejemplares)
            print("\nNuevo libro ingresado")

    elif (opcion == 7):   #Actualizar ejemplares (préstamo/devolución) --------------------------------------------------------------------

        #MUESTRO LOS LIBROS DISPONIBLES PARA ELEGIR
        print("Lista de libros disponibles:\n")
        for i, titulo in enumerate(lista_titulos):
            print(f"{i+1}. {titulo} (Cantidad de ejemplares actuales: {lista_cant_ejemplares[i]})")
    
        titulo = -1
        while titulo < 1 or titulo > len(lista_titulos):
            titulo_input = input("\nIngrese el número del libro que desea elegir: ")
            if titulo_input.isdigit():
                titulo = int(titulo_input)
                if titulo < 1 or titulo > len(lista_titulos):
                    print("Opción no válida. Ingrese un número de libro válido.")
            else:
                print("Opción no válida. Ingrese un número de libro válido.")
        titulo -= 1

        # VALIDO QUE SEA LA OPCION CORRECTA
        if (1 <= titulo <=len(lista_titulos)):
             
             prestamo_devolucion = (input("\nEscriba si desea un Préstamo o una Devolución: "))

             # VALIDO QUE SEA UNA OPCION CORRECTA
             while (prestamo_devolucion not in ["Préstamo","Prestamo", "prestamo", "Devolución","Devolucion","devolucion"]):
                    prestamo_devolucion = (input("\nEscriba si desea un Préstamo o una Devolución: "))

             # SI ES PRESTAMO
             if (prestamo_devolucion in ["Préstamo","Prestamo", "prestamo"]):

                # VALIDO QUE HAYA EJEMPLARES PARA PRESTAR 
                if (lista_cant_ejemplares[titulo] == 0):
                 print ("No hay ejemplares disponibles")                 
                else:
                 lista_cant_ejemplares[titulo] -= 1
                 print(f"Préstamo realizado, cantidad de títulos disponibles: {lista_cant_ejemplares[titulo]}")
             
             # SI ES DEVOLUCION
             if (prestamo_devolucion in ["Devolución","Devolucion","devolucion"]):
                 lista_cant_ejemplares[titulo] += 1
                 print(f"Devolución realizado, cantidad de títulos disponibles: {lista_cant_ejemplares[titulo]}")     
    
        else:
            print("\nOpción no válida")

    
    elif (opcion == 8):   #Salir-----------------------------------------------------------------------------------------------------------
        print ("¡Hasta Luego!")

    opcion_valida = False # VUELVO A COLOCAR EN FALSE PARA QUE VUELVA A VALIDAR LA OPCION

#----FIN DEL PROGRAMA----#
