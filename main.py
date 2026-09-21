from dominio.empleado import Empleado
from dominio.area import Area
from dominio.departamento import Departamento
from dominio.registroTiempo import RegistroTiempo
from dominio.proyecto import Proyecto

ana = Empleado(
    nombre="Ana Torres",
    correo="ana.torres@echotech.cl",
    telefono="56 9 4728 5932"
)

german = Empleado(
    nombre="German Sopico",
    correo="german.manso@echotech.cl",
    telefono="56 9 8923 1455"
)

area = Area(
    esp="contabilidad",
    emp="Ana Torres"
)

desarrollo = Departamento(
    nombre="Desarrollo"
)


print(ana.mostrar_datos())
print(area.mostrar_area())

desarrollo.agregar_empleado(ana)
print(desarrollo.cantidad_empleados())

desarrollo.agregar_empleado(german)
print(desarrollo.cantidad_empleados())

for empleado in desarrollo.empleados:
    print(empleado.mostrar_datos())

proyecto_eco = Proyecto(
    id=1, 
    nombre="Echotech POO", 
    descripcion="Sistema Base", 
    fechaInicio=20260916
)


Tiempo1 = RegistroTiempo(
    id=101,
    proyecto=proyecto_eco,       
    horas=2.5,                   
    detalle="Modelado de datos", 
    fecha="25/09/26"            
)

print ( " Registro de tiempo")
print(f"proyecto: {Tiempo1.proyecto.nombre}")
print(f"Detalle: {Tiempo1.detalle}")
print(f"Resultado: {Tiempo1.mostrar_tiempo()}")

