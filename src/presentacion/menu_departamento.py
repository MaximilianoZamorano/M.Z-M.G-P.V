from dominio.departamento import Departamento
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.empleado_dao import EmpleadoDAO

def registrar_departamento():
    print("\n--- Registrar Nuevo Departamento ---")
    try:
        nombre = input("Nombre del departamento: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        gerente_input = input("ID del empleado Gerente (Enter para omitir): ").strip()
        departamento = Departamento(nombre=nombre)
        
        if gerente_input:
            gerente = EmpleadoDAO.obtenerPorId(int(gerente_input))
            if gerente:
                departamento.asignarGerente(gerente)

        dep_registrado = DepartamentoDAO.insertar(departamento)
        print(f"Departamento registrado correctamente con ID: {dep_registrado.id}")
    except Exception as e:
        print(f"Error al registrar: {e}")

def listar_departamentos():
    print("\n--- Lista de Departamentos ---")
    try:
        lista = DepartamentoDAO.listar()
        if not lista:
            print("No hay departamentos registrados.")
            return
        for dep in lista:
            info_gerente = f"| Gerente ID: {dep.gerente_id}" if getattr(dep, 'gerente_id', None) else "| Sin Gerente"
            print(f"ID: {dep.id} | Nombre: {dep.nombre} {info_gerente}")
    except Exception as e:
        print(f"Error al listar: {e}")

def buscar_departamento():
    print("\n--- Buscar Departamento ---")
    try:
        id_dep = int(input("Ingrese ID del departamento: "))
        dep = DepartamentoDAO.obtenerPorId(id_dep)
        if dep:
            info_gerente = f"ID Gerente: {dep.gerente_id}" if getattr(dep, 'gerente_id', None) else "Sin asignar"
            print(f"ID: {dep.id} | Nombre: {dep.nombre} | {info_gerente}")
        else:
            print("No se encontró el departamento.")
    except ValueError:
        print("Error: El ID debe ser un número.")

def actualizar_departamento():
    print("\n--- Actualizar Departamento ---")
    try:
        id_dep = int(input("Ingrese ID del departamento: "))
        dep = DepartamentoDAO.obtenerPorId(id_dep)
        if not dep:
            print("Departamento no encontrado.")
            return

        nuevo_nombre = input(f"Nuevo nombre [{dep.nombre}]: ").strip()
        if nuevo_nombre: dep.nombre = nuevo_nombre

        gerente_input = input("ID del nuevo Gerente (Enter para mantener): ").strip()
        if gerente_input:
            gerente = EmpleadoDAO.obtenerPorId(int(gerente_input))
            if gerente: dep.asignarGerente(gerente)

        if DepartamentoDAO.actualizar(dep):
            print("Departamento actualizado.")
        else:
            print("No se pudo actualizar.")
    except Exception as e:
        print(f"Error al actualizar: {e}")

def eliminar_departamento():
    print("\n--- Eliminar Departamento ---")
    try:
        id_dep = int(input("Ingrese ID a eliminar: "))
        if DepartamentoDAO.eliminar(id_dep):
            print("Departamento eliminado.")
        else:
            print("No se encontró el departamento.")
    except ValueError:
        print("Error: El ID debe ser un número.")

def mostrar_menu_departamento():
    print("\n===== GESTIÓN DE DEPARTAMENTOS =====")
    print("1. Registrar departamento")
    print("2. Listar departamentos")
    print("3. Buscar departamento")
    print("4. Actualizar departamento")
    print("5. Eliminar departamento")
    print("0. Volver al menú principal")

def menu_departamento():
    while True:
        mostrar_menu_departamento()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1": registrar_departamento()
        elif opcion == "2": listar_departamentos()
        elif opcion == "3": buscar_departamento()
        elif opcion == "4": actualizar_departamento()
        elif opcion == "5": eliminar_departamento()
        elif opcion == "0": break
        else: print("Opción no válida.")