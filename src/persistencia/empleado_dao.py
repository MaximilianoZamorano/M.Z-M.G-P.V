# persistencia/empleado_dao.py
from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.empleado import Empleado

class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            INSERT INTO empleado (nombre, direccion, telefono, email, fechaInicioContrato, salario, departamento_id)
            VALUES ({marca}, {marca}, {marca}, {marca}, {marca}, {marca}, {marca})
        """
        cursor.execute(sql, (
            empleado.nombre, 
            empleado.direccion, 
            empleado.telefono, 
            empleado.email, 
            empleado.fechaInicioContrato, 
            empleado.salario, 
            empleado.departamento_id
        ))
        empleado.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return empleado
    
    @staticmethod
    def eliminar(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"DELETE FROM empleado WHERE id = {marca}"
        cursor.execute(sql, (id_empleado,))
        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado

    @staticmethod
    def obtenerPorId(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            SELECT id, nombre, direccion, telefono, email, fechaInicioContrato, salario, departamento_id
            FROM empleado WHERE id = {marca}
        """
        cursor.execute(sql, (id_empleado,))
        fila = cursor.fetchone()
        conexion.close()
        
        if fila is None:
            return None
        
        return EmpleadoDAO._fila_a_empleado(fila)

    @staticmethod
    def actualizar(empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                UPDATE empleado 
                SET nombre = {marca}, direccion = {marca}, telefono = {marca}, 
                    email = {marca}, fechaInicioContrato = {marca}, 
                    salario = {marca}, departamento_id = {marca}
                WHERE id = {marca}
            """
            cursor.execute(
                sql,
                (
                    empleado.nombre,
                    empleado.direccion,
                    empleado.telefono,
                    empleado.email,
                    empleado.fechaInicioContrato,
                    empleado.salario,
                    empleado.departamento_id,
                    empleado.id
                )
            )
            conexion.commit()
            return cursor.rowcount > 0
    
        except Exception:
            if conexion:
                conexion.rollback()
            raise   
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id, nombre, direccion, telefono, email, fechaInicioContrato, salario, departamento_id 
            FROM empleado
        """)
        filas = cursor.fetchall()
        conexion.close()
        
        empleados = []
        for fila in filas:
            empleados.append(EmpleadoDAO._fila_a_empleado(fila))
            
        return empleados

    @staticmethod
    def _fila_a_empleado(fila):
        # Transforma el registro devuelto por la BD en un objeto Empleado
        return Empleado(
            id=fila[0],
            nombre=fila[1],
            direccion=fila[2],
            telefono=fila[3],
            email=fila[4],
            fechaInicioContrato=fila[5],
            salario=fila[6],
            departamento_id=fila[7]
        )

