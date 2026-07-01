def generar_legajos():

    legajos = []
    for i in range(15):
        legajos.append(101 + i)
    
    return legajos

def iniciar_recaudacion():
    """
    crea la matriz de recaudacion
    """
    matriz = []
    for i in range(3):
        fila = [0.0, 0.0, 0.0, 0.0, 0.0]
        matriz.append(fila)

    return matriz

def validar_legajo(legajo_ingresado, lista_legajo):
    for legajo_existente in lista_legajo:
        if legajo_ingresado == legajo_existente:
            return True
    return False

def solicitar_linea():

    while True:
        try:
            linea = int(input("Ingrese el numero de linea(1-3): "))
            if 1 <= linea <= 3:
                return linea -1
            print("Linea invalida, debe ser 1, 2 o 3")
        except ValueError:
            print("porfavor, ingrese el numero entero")

def solicitar_coche():

    while True:
        try:
            coche = int(input("Ingrese el numero de coche(1-5):"))
            if 1 <= coche <= 5:
                return coche -1
            print("coche invalido, debe ser de 1 al 5")
        except ValueError:
            print("por favor, Ingrese el numero entero")

def solicitar_monto():

    while True:
        try:
            monto_dinero = float(input("Ingrese el monto recaudado: $"))
            if monto_dinero >= 0:
                return monto_dinero
            print("el monto no puede ser negativo")
        except ValueError:
          print("monto invalido. Ingrese el valor del numero")



def cargar_plantilla(matriz_recaudacion, lista_legajos):
    print("---CARGA DE RECAUDACION---")
    try:
        identificador = int(input("Ingrese su numero de legajo: "))
    except ValueError:
        print("legajo invalido. debe ser un numero")
        return

    if not validar_legajo(identificador, lista_legajos):
        print("el legajo ingresado no existe en el sistema")
        return

    print(f"chofer autorizado(legajo: {identificador})") 
    linea_idx = solicitar_linea()
    coche_idx = solicitar_coche()
    pago = solicitar_monto()


    matriz_recaudacion[linea_idx][coche_idx] += pago
    print(f"recaudacion de pago ${pago:.2f} registrada con exito")

def mostrar_matriz_recaudacion(matriz):
    print("---MATRIZ DE RECAUDACION TOTAL---")
    print("linea/coche")
    for i in range(len(matriz)):
        print(f"linea{i+1}: ", end="")

        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
        
    print()

def recaudacion_por_linea(matriz):
    print("---TOTAL POR LINEA---")
    for i in range(len(matriz)):
        total_linea = 0
        for j in range(len(matriz[i])):
            total_linea += matriz[i][j]
        print(f"linea {i+1}: ${total_linea:.2f}")


def recaudacion_por_coche(matriz):
    print("---TOTAL POR COCHE---")
    coche_idx = solicitar_coche()


    total_coche = 0
    for i in range(len(matriz)):
        total_coche += matriz[i][coche_idx]


    print(f"recaudacion total acumilada del coche {coche_idx + 1}: ${total_coche:.2f}")

def recaudacion_total(matriz):
    total = 0 

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += matriz[i][j]

    print(f"Recaudacion total acumulada: ${total:.2f}")



def men():

    """
    muestra el menu del sistema
    """
    legajos_sistema = generar_legajos()
    recaudaciones = iniciar_recaudacion()

    print("los legajos validos para hoy son del 101 al 115")


    while True:
        print("      SISTEMA DE GESTION DE TRANSPORTE     ")
        print("1. cargar plantilla de recaudacion")
        print("2. Mostrar la recaudacion de cada coche y linea")
        print("3. calcular y mostrar la recaudacion de linea")
        print("4. calcular y mostrar la recaudacion del coche")
        print("5. calcular y mostrar la recaudacion total")
        print("6. salir del programa")


        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            cargar_plantilla(recaudaciones, legajos_sistema)
        elif opcion == "2":
            mostrar_matriz_recaudacion(recaudaciones)
        elif opcion == "3":
            recaudacion_por_linea(recaudaciones)
        elif opcion == "4":
            recaudacion_por_coche(recaudaciones)
        elif opcion == "5":
             recaudacion_total(recaudaciones)
        elif opcion == "6":
            print(f"gracias por utilizar el sistema, saliendo...")
            break
        else:
            print("opcion invalida. intente de nuevo")


if __name__ =="__main__":
     men()