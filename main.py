from encargado import Encargado
from estudiante import Estudiante
from equipo import Equipo

from base_datos import (
    crear_base_datos,
    guardar_equipo,
    guardar_estudiante,
    guardar_encargado,
    actualizar_equipo,
    actualizar_estudiante,
    cargar_equipos,
    cargar_estudiantes,
    cargar_encargados
)


equipos = []
estudiantes = []
encargados = []


def buscar_equipo(id_equipo):

    for equipo in equipos:

        if equipo.id == id_equipo:
            return equipo

    return None


def iniciar_sesion(tipo_usuario):

    id_usuario = input("Ingrese su ID: ")
    password = input("Ingrese su contraseña: ")

    if tipo_usuario == "Encargado":

        for encargado in encargados:

            if (id_usuario == encargado.id and
                    password == encargado.password):

                return encargado

    elif tipo_usuario == "Estudiante":

        for estudiante in estudiantes:

            if (id_usuario == estudiante.id and
                    password == estudiante.password):

                return estudiante

    return None


def crear_encargado():

    print("\n--- CREAR USUARIO ENCARGADO ---")

    id_encargado = input("ID: ")
    cuenta = input("Nombre de usuario(Alias): ")
    password = input("Contraseña: ")
    correo = input("Correo: ")

    if " " in id_encargado:
        print("El ID no es válido. No se permiten espacios.")
        return

    if " " in cuenta:
        print("El usuario no es válido. No se permiten espacios.")
        return

    if " " in password:
        print("La contraseña no es válida. No se permiten espacios.")
        return

    encargado = Encargado(
        id_encargado,
        cuenta,
        password,
        correo,
        "Encargado"
    )

    encargados.append(encargado)
    guardar_encargado(encargado)
    print("Usuario encargado creado correctamente.")



def crear_estudiante():

    print("\n--- CREAR USUARIO ESTUDIANTE ---")

    id_estudiante = input("ID: ")
    nombre = input("Nombre: ")
    password = input("Contraseña: ")
    correo = input("Correo: ")
    telefono = input("Teléfono: ")

    if " " in id_estudiante:
        print("El ID no es válido. No se permiten espacios.")
        return

    if " " in password:
        print("La contraseña no es válida. No se permiten espacios.")
        return

    estudiante = Estudiante(
        id_estudiante,
        nombre,
        password,
        correo,
        "Estudiante",
        telefono
    )

    estudiantes.append(estudiante)
    guardar_estudiante(estudiante)
    print("Usuario estudiante creado correctamente.")


def menu_acceso_encargado():

    while True:

        print("\n==============================")
        print("          ENCARGADO")
        print("==============================")
        print("1. Crear usuario")
        print("2. Ingresar")
        print("3. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_encargado()

        elif opcion == "2":
            usuario = iniciar_sesion("Encargado")

            if usuario != None:
                print("\nBienvenido", usuario.cuenta)
                menu_encargado(usuario)

            else:
                print("\nID o contraseña incorrectos.")

        elif opcion == "3":
            break

        else:
            print("Opción no válida.")


def menu_acceso_estudiante():

    while True:

        print("\n==============================")
        print("         ESTUDIANTE")
        print("==============================")
        print("1. Crear usuario")
        print("2. Ingresar")
        print("3. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_estudiante()

        elif opcion == "2":
            usuario = iniciar_sesion("Estudiante")

            if usuario != None:
                print("\nBienvenido", usuario.nombre)
                menu_estudiante(usuario)

            else:
                print("\nID o contraseña incorrectos.")

        elif opcion == "3":
            break

        else:
            print("Opción no válida.")


def menu_encargado(encargado):

    while True:

        print("\n==============================")
        print("       MENÚ ENCARGADO")
        print("==============================")
        print("1. Consultar inventario")
        print("2. Registrar equipo")
        print("3. Registrar estudiante")
        print("4. Consultar estudiantes")
        print("5. Consultar estado de equipo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            encargado.consultar_inventario(equipos)

        elif opcion == "2":
            id_equipo = input("ID del equipo: ")
            nombre = input("Nombre del equipo: ")
            cantidad = int(input("Cantidad: "))
            equipo = Equipo(
                id_equipo,
                nombre,
                cantidad,
                "Disponible"
            )

            encargado.registrar_equipo(
                equipos,
                equipo
            )

            guardar_equipo(equipo)

        elif opcion == "3":
            id_estudiante = input("ID del estudiante: ")
            nombre = input("Nombre: ")
            password = input("Contraseña: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            estudiante = Estudiante(
                id_estudiante,
                nombre,
                password,
                correo,
                "Estudiante",
                telefono
            )

            encargado.registrar_persona(
                estudiantes,
                estudiante
            )

            guardar_estudiante(estudiante)

        elif opcion == "4":
            encargado.consultar_estudiante(
                estudiantes
            )

        elif opcion == "5":
            id_equipo = input(
                "Ingrese el ID del equipo: "
            )
            equipo = buscar_equipo(id_equipo)

            if equipo != None:
                equipo.consultar_estado()

            else:
                print("Equipo no encontrado.")

        elif opcion == "6":
            print("Sesión finalizada.")
            break

        else:
            print("Opción no válida.")


def menu_estudiante(estudiante):

    while True:
        print("\n==============================")
        print("       MENÚ ESTUDIANTE")
        print("==============================")
        print("1. Consultar inventario")
        print("2. Solicitar préstamo")
        print("3. Consultar estado de equipo")
        print("4. Actualizar información")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante.consultar_inventario(equipos)

        elif opcion == "2":
            id_equipo = input(
                "Ingrese el ID del equipo: "
            )

            equipo = buscar_equipo(id_equipo)

            if equipo != None:
                estudiante.solicitar_prestamo(equipo)
                actualizar_equipo(equipo)

            else:
                print("Equipo no encontrado.")

        elif opcion == "3":
            id_equipo = input(
                "Ingrese el ID del equipo: "
            )

            equipo = buscar_equipo(id_equipo)

            if equipo != None:
                estudiante.consultar_equipo(equipo)

            else:
                print("Equipo no encontrado.")

        elif opcion == "4":
            correo = input("Nuevo correo: ")
            telefono = input("Nuevo teléfono: ")

            estudiante.actualizar_info(
                correo,
                telefono
            )

            actualizar_estudiante(estudiante)

        elif opcion == "5":
            print("Sesión finalizada.")
            break

        else:
            print("Opción no válida.")


def menu_principal():

    while True:

        print("\n==============================")
        print("   SISTEMA DE INVENTARIO")
        print("==============================")
        print("1. Encargado")
        print("2. Estudiante")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_acceso_encargado()

        elif opcion == "2":
            menu_acceso_estudiante()

        elif opcion == "3":
            print("\nPrograma finalizado.")
            break

        else:
            print("Opción no válida.")


crear_base_datos()

equipos = cargar_equipos()
estudiantes = cargar_estudiantes()
encargados = cargar_encargados()

menu_principal()