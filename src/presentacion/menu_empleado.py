from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

def registrar_empleado():
    print("\n--- Registrar Nuevo Empleado ---")
    try:
        nombre = input("Nombre: ").strip()
        direccion = input("Dirección: ").strip()
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        fechaInicioContrato = input("Fecha de inicio contrato (YYYY-MM-DD): ").strip()
        salario = float(input("Salario: "))
        
        dep_input = input("ID de Departamento (presione Enter para omitir): ").strip()
        departamento_id = int(dep_input) if dep_input else None

        empleado = Empleado(nombre, direccion, telefono, email, fechaInicioContrato, salario, departamento_id)
        empleado_registrado = EmpleadoDAO.insertar(empleado)
        print(f"Empleado registrado correctamente con el ID: {empleado_registrado.id}")
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
    except Exception as e:
        print(f"No fue posible registrar el empleado: {e}")

def listar_empleados():
    print("\n--- Lista de Empleados ---")
    try:
        lista = EmpleadoDAO.listar()
        if not lista:
            print("No hay empleados registrados.")
            return
        for empleado in lista:
            print(f"ID: {empleado.id} | {empleado.mostrar_datos()}")
    except Exception as e:
        print(f"Error al listar empleados: {e}")

def buscar_empleado():
    print("\n--- Buscar Empleado ---")
    try:
        id_empleado = int(input("Ingrese el ID del empleado a buscar: "))
        empleado = EmpleadoDAO.obtenerPorId(id_empleado)
        if empleado:
            print(f"ID: {empleado.id} | {empleado.mostrar_datos()}")
        else:
            print("No se encontró ningún empleado con ese ID.")
    except ValueError:
        print("Error: El ID debe ser un número.")

def actualizar_empleado():
    print("\n--- Actualizar Empleado ---")
    try:
        id_empleado = int(input("Ingrese el ID del empleado a actualizar: "))
        empleado = EmpleadoDAO.obtenerPorId(id_empleado)
        if not empleado:
            print("No se encontró ningún empleado con ese ID.")
            return

        nombre = input(f"Nombre [{empleado.nombre}]: ").strip()
        direccion = input(f"Dirección [{empleado.direccion}]: ").strip()
        telefono = input(f"Teléfono [{empleado.telefono}]: ").strip()
        email = input(f"Email [{empleado.email}]: ").strip()
        salario_input = input(f"Salario [{empleado.salario}]: ").strip()

        empleado.actualizarDatos(
            nombre=nombre if nombre else None,
            direccion=direccion if direccion else None,
            telefono=telefono if telefono else None,
            email=email if email else None,
            salario=float(salario_input) if salario_input else None
        )

        if EmpleadoDAO.actualizar(empleado):
            print("Empleado actualizado correctamente.")
        else:
            print("No se pudo actualizar el empleado.")
    except Exception as e:
        print(f"Error al actualizar: {e}")

def eliminar_empleado():
    print("\n--- Eliminar Empleado ---")
    try:
        id_empleado = int(input("Ingrese el ID del empleado a eliminar: "))
        if EmpleadoDAO.eliminar(id_empleado):
            print("Empleado eliminado correctamente.")
        else:
            print("No se encontró ningún empleado con ese ID.")
    except ValueError:
        print("Error: El ID debe ser un número.")

def mostrar_menu_empleado():
    print("\n===== GESTIÓN DE EMPLEADOS =====")
    print("1. Registrar empleado")
    print("2. Listar empleados")
    print("3. Buscar empleado")
    print("4. Actualizar empleado")
    print("5. Eliminar empleado")
    print("0. Volver al menú principal")

def menu_empleado():
    while True:
        mostrar_menu_empleado()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1": registrar_empleado()
        elif opcion == "2": listar_empleados()
        elif opcion == "3": buscar_empleado()
        elif opcion == "4": actualizar_empleado()
        elif opcion == "5": eliminar_empleado()
        elif opcion == "0": break
        else: print("Opción no válida.")