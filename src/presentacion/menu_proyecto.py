from dominio.proyecto import Proyecto
from persistencia.proyecto_dao import ProyectoDAO

def registrar_proyecto():
    print("\n--- Registrar Nuevo Proyecto ---")
    try:
        nombre = input("Nombre del proyecto: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        descripcion = input("Descripción: ").strip()
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
        
        proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fechaInicio=fecha_inicio)
        
        proy_registrado = ProyectoDAO.insertar(proyecto)
        print(f"Proyecto registrado correctamente con el ID: {proy_registrado.id}")
    except Exception as e:
        print(f"No fue posible registrar el proyecto: {e}")

def listar_proyectos():
    print("\n--- Lista de Proyectos ---")
    try:
        lista = ProyectoDAO.listar()
        if not lista:
            print("No hay proyectos registrados.")
            return
        
        for proy in lista:
            print(f"ID: {proy.id} | Nombre: {proy.nombre} | Fecha Inicio: {proy.fechaInicio}")
    except Exception as e:
        print(f"Error al listar proyectos: {e}")

def buscar_proyecto():
    print("\n--- Buscar Proyecto ---")
    try:
        id_proy = int(input("Ingrese el ID del proyecto a buscar: "))
        proy = ProyectoDAO.obtenerPorId(id_proy)
        
        if proy:
            print(f"ID: {proy.id} | Nombre: {proy.nombre}")
            print(f"Descripción: {proy.descripcion}")
            print(f"Fecha Inicio: {proy.fechaInicio}")
        else:
            print("No se encontró ningún proyecto con ese ID.")
    except ValueError:
        print("Error: El ID debe ser un número.")
    except Exception as e:
        print(f"Error al buscar el proyecto: {e}")

def actualizar_proyecto():
    print("\n--- Actualizar Proyecto ---")
    try:
        id_proy = int(input("Ingrese el ID del proyecto a actualizar: "))
        proy = ProyectoDAO.obtenerPorId(id_proy)
        
        if not proy:
            print("No se encontró ningún proyecto con ese ID.")
            return

        print("Deje el campo en blanco y presione Enter si NO desea modificarlo.")
        nombre = input(f"Nuevo nombre [{proy.nombre}]: ").strip()
        descripcion = input(f"Nueva descripción [{proy.descripcion}]: ").strip()
        fecha_inicio = input(f"Nueva fecha inicio [{proy.fechaInicio}]: ").strip()

        if nombre: proy.nombre = nombre
        if descripcion: proy.descripcion = descripcion
        if fecha_inicio: proy.fechaInicio = fecha_inicio

        if ProyectoDAO.actualizar(proy):
            print("Proyecto actualizado correctamente.")
        else:
            print("No se pudo actualizar el proyecto.")
    except Exception as e:
        print(f"Error al actualizar el proyecto: {e}")

def eliminar_proyecto():
    print("\n--- Eliminar Proyecto ---")
    try:
        id_proy = int(input("Ingrese el ID del proyecto a eliminar: "))
        if ProyectoDAO.eliminar(id_proy):
            print("Proyecto eliminado correctamente.")
        else:
            print("No se encontró ningún proyecto con ese ID.")
    except ValueError:
        print("Error: El ID debe ser un número.")
    except Exception as e:
        print(f"Error al eliminar el proyecto: {e}")

def mostrar_menu_proyecto():
    print("\n===== GESTIÓN DE PROYECTOS =====")
    print("1. Registrar proyecto")
    print("2. Listar proyectos")
    print("3. Buscar proyecto")
    print("4. Actualizar proyecto")
    print("5. Eliminar proyecto")
    print("0. Volver al menú principal")

def menu_proyecto():
    while True:
        mostrar_menu_proyecto()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1": registrar_proyecto()
        elif opcion == "2": listar_proyectos()
        elif opcion == "3": buscar_proyecto()
        elif opcion == "4": actualizar_proyecto()
        elif opcion == "5": eliminar_proyecto()
        elif opcion == "0": break
        else: print("Opción no válida. Intente nuevamente.")