def mostrar_menu():
    print("------------------")
    print("  Menú Principal  ")
    print("------------------")
    print("(1). Registro Propietario")
    print("(2). Abono Propietario")
    print("(3). Agregar Cuota especial")
    print("(4). Salir")
    print("------------------")

while True:
    mostrar_menu()
    opcion = int(input("Digite una opción: "))

    if opcion == 1:
        print("Creando el Registro del Propietario ...")
        # Implementar la funcionalidad de la opción 1
        nombre = str(input("Escriba el nombre del propietario: "))
        apellido = str(input("Escriba el Apellido del propietario: "))
        numero_de_casa = int(input("Escriba el numero de casa del propietario: "))
        numero_de_telefono = int(input("Escriba el numero del telefono del propietario: "))
        deuda_acumulada_bolivares = int(input("Ingrese la deuda acumulada del propietario en bolivares: "))
        deuda_acumulada_dolares = int(input("Ingrese la deuda acumulada del propietario en dolares: "))
        print("Propietario Registrado exitosamente")
        print(nombre)
        print(apellido)
        print(numero_de_casa)
        print(numero_de_telefono)
        print(deuda_acumulada_bolivares)
        print(deuda_acumulada_dolares)
    elif opcion == 2:
        print("Creando el abono del propietario ...")
        # Implementar la funcionalidad de la opción 2
    elif opcion == 3:
        print("Agregando Cuota Espcecial1")
        # Implementar la funcionalidad de la opción 3
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")