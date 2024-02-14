import pymysql

'''
conexion = pymysql.connect(
    host="localhost",
    user="usuario",
    password="contraseña",
    database="nombre_de_la_base_de_datos",
)
cursor = conexion.cursor()
'''

def mostrar_menu():
    print("------------------")
    print("  Menú Principal  ")
    print("------------------")
    print("(1). Registro Propietario")
    print("(2). Consulta Deuda Propietario")
    print("(3). Abono Propietario")
    print("(4). Agregar Cuota especial")
    print("(5). Salir")
    print("------------------")


while True:
    mostrar_menu()
    opcion = int(input("Digite una opción: "))

    if opcion == 1:
        # Implementar la funcionalidad de la opción 1
        print("Creando el Registro del Propietario ...")
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
        print("------------------")
        print("  Menú Principal  ")
        print("------------------")
        print("(1). Consulta deuda del propietario")
        print("(2). Consulta Deuda general")
        print("(3). Salir")
        print("------------------")

        consultar_deuda_opcion = int(input("Digite una opción: "))

        while True:

                if consultar_deuda_opcion == 1:
                    print("Consulta de deuda del propietario ...")
                    numero_de_casa = int(input("Escriba el numero de casa del propietario: "))
                    break
                elif consultar_deuda_opcion == 2:
                    print("Consulta de deuda general de los propietarios ...")
                    break

                elif consultar_deuda_opcion == 3:
                    print("saliendo del submenu")
                    break
                else:
                    print("opcion no valida.")
                    break

    elif opcion == 3:
        # Implementar la funcionalidad de la opción 3
        print("Creando el abono del propietario ...")
    elif opcion == 4:
        # Implementar la funcionalidad de la opción 4
        print("Agregando Cuota Espcecial1")
    elif opcion == 5:
        print("Saliendo del programa..5.")
        break
    else:
        print("Opción no válida.")
