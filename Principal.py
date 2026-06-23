#ingreso inicial
usuario = ""
contraseña = ""
opcion = ""

print("Registrese")

usuario = input("Cree un nombre de usuario: ")
contraseña = input("Cree una contraseña: ")

correcto = False
#VALIDACION
while correcto == False:
    contraseña1 = input(f"Ingrese su contraseña {usuario}: ")

    if contraseña1 == contraseña:
        correcto = True
    else:
        print("Error, contraseña incorrecta, ingrese nuevamente la contraseña: ")
print("Acceso concedido, bienvenido", usuario)

#MENU
while opcion != "6":
    print("1 Proyectos")
    print("2 Tablas ")
    print("3 Variables")
    print("4 Mostrar")
    print("5 Estadisticas")
    print("6 Salir")

    opcion = input("Elija la opcion que desea ver: ")

    match opcion:
        case "1":
            print("Proyectos")
        case "2":
            print("Tablas")
        case "3":
            print("Variables")
        case "4":
            print("Información")
        case "5":
            print("Estadistica")
        case "6":
            print("Salir, fin del programa")
