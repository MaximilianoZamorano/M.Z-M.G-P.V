from dominio.empleado import Empleado
from dominio.area import Area
from dominio.departamento import Departamento
from dominio.registroTiempo import RegistroTiempo
from dominio.proyecto import Proyecto
from persistencia.crear_db import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO


crear_tablas()
empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl", telefono=9133)

print("Antes:", empleado.id)
# None

EmpleadoDAO.insertar(empleado)
print("Después:", empleado.id)
# id generado por la BD

EmpleadoDAO.insertar(empleado)
encontrado = EmpleadoDAO.buscar_por_id(empleado.id)
print("Encontrado:", encontrado.mostrar_datos())
print("Listado:")
for item in EmpleadoDAO.listar():
    print(item.mostrar_datos())

