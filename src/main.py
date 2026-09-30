from dominio.empleado import Empleado
from dominio.area import Area
from dominio.departamento import Departamento
from dominio.registroTiempo import RegistroTiempo
from dominio.proyecto import Proyecto
from persistencia.crear_db import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

def registrar_empleado():
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    telefono = input("telefono: ").strip()
    empleado = Empleado(nombre, correo, telefono)
    try:
        EmpleadoDAO.insertar(empleado)
        print("Empleado registrado correctamente.")
    except Exception:
        print("No fue posible registrar el empleado.")


def mostrar_menu():
    print("\n===== ECOTECH =====")
    print("1. Registrar empleado")
    print("2. Listar empleados")
    print("3. Buscar empleado")
    print("4. Actualizar empleado")
    print("5. Eliminar empleado")
    print("0. Salir")

def listar_empleados():
    
    lista = EmpleadoDAO.listar()
    for empleado in lista:
        print(empleado.mostrar_datos())


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            listar_empleados()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()


