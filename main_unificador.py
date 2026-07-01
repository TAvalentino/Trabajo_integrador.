from principal2.validaciones.funciones import validar_rango, es_par, es_primo, es_multiplo
import principal3

def cuerpo_unificador():
    print("=== REGISTRESE ===")
    usuario = input("Cree un nombre de usuario: ")
    contraseña = input("Cree una contraseña: ")

    correcto = False
    while not correcto:
        contraseña1 = input(f"Ingrese su contraseña {usuario}: ")
        if contraseña1 == contraseña:
            correcto = True
        else:
            print("Error, contraseña incorrecta. Ingrese nuevamente.")
            
    print(f"\nAcceso concedido, bienvenido {usuario}\n")

    legajos_sistema = principal3.generar_legajos()
    recaudaciones = principal3.iniciar_recaudacion()

    opcion = ""
    while opcion != "6":
        print("\n--- MENU ---")
        print("1 Proyectos")
        print("2 Tablas ")
        print("3 Variables")
        print("4 Mostrar")
        print("5 Estadisticas")
        print("6 Salir")

        opcion = input("Elija la opcion que desea ver: ")

        match opcion:
            case "1":
                print("\nEntrando a Proyectos: Sistema de Gestión de Transporte")
                principal3.men() 
            case "2":
                print("Tablas")
            case "3":
                print("Variables")
            case "4":
                print("Información")
                principal3.mostrar_matriz_recaudacion(recaudaciones)
            case "5":
                print("\nESTADÍSTICAS Y PROPIEDADES MATEMÁTICAS")
                try:
                    num = int(input("Ingrese un número entero para analizar: "))

                    if es_par(num):
                        print(f"El número {num} es: PAR")
                    else:
                        print(f"El número {num} es: IMPAR")

                    if es_primo(num):
                        print(f"El número {num} es: PRIMO")
                    else:
                        print(f"El número {num} NO es primo")

                    if es_multiplo(num, 5):
                        print(f"El número {num} es: MÚLTIPLO DE 5")
                    else:
                        print(f"El número {num} NO es múltiplo de 5")

                    if validar_rango(num, 1, 100):
                        print(f"El número {num} está dentro del rango estándar (1 a 100)")
                    else:
                        print(f"El número {num} está FUERA del rango estándar (1 a 100)")

                except ValueError:
                    print("Error: Debe ingresar un número entero válido.")
            case "6":
                print("Salir, fin del programa")
            case _:
                print(" Opción no válida. Intente otra vez.")

if __name__ == "__main__":
    cuerpo_unificador()