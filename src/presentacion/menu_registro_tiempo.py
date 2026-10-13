from dominio.registro_tiempo import RegistroTiempo
from persistencia.registro_tiempo_dao import RegistroTiempoDAO
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.proyecto_dao import ProyectoDAO

def registrar_tiempo():
    print("\n--- Registrar Tiempo Trabajado ---")
    try:
        empleado_id = int(input("ID del Empleado: "))
        if not EmpleadoDAO.obtenerPorId(empleado_id):
            print("Error: No existe un empleado con ese ID.")
            return

        proyecto_id = int(input("ID del Proyecto: "))
        if not ProyectoDAO.obtenerPorId(proyecto_id):
            print("Error: No existe un proyecto con ese ID.")
            return

        fecha = input("Fecha del registro (YYYY-MM-DD): ").strip()
        horas = float(input("Cantidad de horas trabajadas: "))
        descripcion = input("Descripción de las tareas: ").strip()

        registro = RegistroTiempo(fecha=fecha, horas=horas, descripcion=descripcion, 
                                  empleado_id=empleado_id, proyecto_id=proyecto_id)
        
        reg_guardado = RegistroTiempoDAO.insertar(registro)
        print(f"Registro guardado exitosamente con ID: {reg_guardado.id}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para ID y horas.")
    except Exception as e:
        print(f"No fue posible guardar el registro: {e}")

def listar_registros():
    print("\n--- Lista de Registros de Tiempo ---")
    try:
        lista = RegistroTiempoDAO.listar()
        if not lista:
            print("No hay registros de tiempo.")
            return
        
        for reg in lista:
            print(f"ID: {reg.id} | Fecha: {reg.fecha} | Horas: {reg.horas} | Emp: {reg.empleado_id} | Proy: {reg.proyecto_id}")
    except Exception as e:
        print(f"Error al listar registros: {e}")

def buscar_registro():
    print("\n--- Buscar Registro de Tiempo ---")
    try:
        id_reg = int(input("Ingrese el ID del registro a buscar: "))
        reg = RegistroTiempoDAO.obtenerPorId(id_reg)
        
        if reg:
            print(f"ID: {reg.id} | Fecha: {reg.fecha} | Horas: {reg.horas}")
            print(f"Empleado ID: {reg.empleado_id} | Proyecto ID: {reg.proyecto_id}")
            print(f"Descripción: {reg.descripcion}")
        else:
            print("No se encontró ningún registro con ese ID.")
    except ValueError:
        print("Error: El ID debe ser un número.")
    except Exception as e:
        print(f"Error al buscar: {e}")

def actualizar_registro():
    print("\n--- Actualizar Registro de Tiempo ---")
    try:
        id_reg = int(input("Ingrese el ID del registro a actualizar: "))
        reg = RegistroTiempoDAO.obtenerPorId(id_reg)
        
        if not reg:
            print("No se encontró ningún registro con ese ID.")
            return

        print("Deje el campo en blanco y presione Enter si NO desea modificarlo.")
        horas_input = input(f"Horas [{reg.horas}]: ").strip()
        descripcion = input(f"Descripción [{reg.descripcion}]: ").strip()

        # Usamos el método modificarRegistro del dominio según el diagrama
        if horas_input or descripcion:
            nuevas_horas = float(horas_input) if horas_input else reg.horas
            nueva_desc = descripcion if descripcion else reg.descripcion
            
            reg.modificarRegistro(nuevas_horas, nueva_desc)

            if RegistroTiempoDAO.actualizar(reg):
                print("Registro actualizado correctamente.")
            else:
                print("No se pudo actualizar.")
    except ValueError:
        print("Error: Las horas deben ser un valor numérico.")
    except Exception as e:
        print(f"Error al actualizar: {e}")

def eliminar_registro():
    print("\n--- Eliminar Registro de Tiempo ---")
    try:
        id_reg = int(input("Ingrese el ID del registro a eliminar: "))
        if RegistroTiempoDAO.eliminar(id_reg):
            print("Registro eliminado correctamente.")
        else:
            print("No se encontró ningún registro con ese ID.")
    except ValueError:
        print("Error: El ID debe ser un número.")
    except Exception as e:
        print(f"Error al eliminar: {e}")

def mostrar_menu_registro():
    print("\n===== GESTIÓN DE TIEMPO =====")
    print("1. Registrar tiempo trabajado")
    print("2. Listar registros")
    print("3. Buscar registro")
    print("4. Actualizar registro")
    print("5. Eliminar registro")
    print("0. Volver al menú principal")

def menu_registro_tiempo():
    while True:
        mostrar_menu_registro()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1": registrar_tiempo()
        elif opcion == "2": listar_registros()
        elif opcion == "3": buscar_registro()
        elif opcion == "4": actualizar_registro()
        elif opcion == "5": eliminar_registro()
        elif opcion == "0": break
        else: print("Opción no válida. Intente nuevamente.")