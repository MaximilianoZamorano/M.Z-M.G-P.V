from presentacion.menu_departamento import menu_departamento
from presentacion.menu_empleado import menu_empleado
from presentacion.menu_proyecto import menu_proyecto
from presentacion.menu_registro_tiempo import menu_registro_tiempo

def mostrar_opciones_principales():
    print("\n===== SISTEMA ECOTECH =====")
    print("1. Gestión de Departamentos")
    print("2. Gestión de Empleados")
    print("3. Gestión de Proyectos")
    print("4. Gestión de Registros de Tiempo")
    print("0. Salir")

def iniciar_menu_principal():
    while True:
        mostrar_opciones_principales()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            menu_departamento()
        elif opcion == "2":
            menu_empleado()
        elif opcion == "3":
            menu_proyecto()
        elif opcion == "4":
            menu_registro_tiempo()
        elif opcion == "0":
            print("Cerrando sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")