# persistencia/empleado_dao.py
from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.empleado import Empleado

class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"
        sql = f"""
            INSERT INTO empleado (nombre, correo, telefono)
            VALUES ({marcador}, {marcador}, {marcador})
        """
        cursor.execute(sql, (empleado.nombre, empleado.correo, empleado.telefono))
        empleado.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return empleado
    

    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
                    SELECT id, nombre, correo, telefono
                    FROM empleado WHERE id = {marca}
        """
        cursor.execute(sql, (id_empleado,))
        fila = cursor.fetchone()
        conexion.close()
        if fila is None:
            return None
        
        return Empleado(id=fila[0], nombre=fila[1], correo=fila[2],telefono=fila[3])
    

    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute(
        "SELECT id, nombre, correo, telefono FROM empleado"
        )
        filas = cursor.fetchall()
        conexion.close()
        empleados = []
        for fila in filas:
            empleados.append(
                Empleado(
                    id=fila[0],
                    nombre=fila[1],
                    correo=fila[2],
                    telefono=fila[3]

                )
            )
        return empleados