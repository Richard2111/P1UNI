def menu_principal():
    print("Bienvenido Programa Duraznos")
    print("    ")
    print("Seleccione su usuario:")
    print("    ")
    print("     1. Propietario")
    print("    ")
    print("     2. Administrador")
    print("    ")
def casas_menu():
    print("Ingrese el numero de su casa, si desea salir ingrese 3")

while True:

    menu_principal()
    tuser = int(input("Ingrese el numero de acuerdo a su eleccion: "))

    if tuser == "1":
        print("Eres propietario.")

    while True:
        casas_menu()
        opcion = int(input("Digite una opción: "))

        if opcion == 1:
            print("Su deuda es 1 bs")

        elif opcion == 2:
            print("Su deuda es 2 bs")

        elif opcion == 3:
            print("Saliendo al menu principal")
            break

        else:
            print("Opción no válida.")

    elif tuser == "2":
        print("Eres Administrador")

    else:
    print("opcion no valida")