from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.registro_tiempo import RegistroTiempo 

class RegistroTiempoDAO:
    @staticmethod
    def insertar(registro):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            INSERT INTO registro_tiempo (fecha, horas, descripcion, empleado_id, proyecto_id)
            VALUES ({marca}, {marca}, {marca}, {marca}, {marca})
        """
        cursor.execute(sql, (
            registro.fecha, 
            registro.horas, 
            registro.descripcion, 
            registro.empleado_id, 
            registro.proyecto_id
        ))
        registro.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return registro
    
    @staticmethod
    def eliminar(id_registro):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"DELETE FROM registro_tiempo WHERE id = {marca}"
        cursor.execute(sql, (id_registro,))
        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado

    @staticmethod
    def obtenerPorId(id_registro):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            SELECT id, fecha, horas, descripcion, empleado_id, proyecto_id
            FROM registro_tiempo WHERE id = {marca}
        """
        cursor.execute(sql, (id_registro,))
        fila = cursor.fetchone()
        conexion.close()
        
        if fila is None:
            return None
        
        return RegistroTiempoDAO._fila_a_registro(fila)

    @staticmethod
    def actualizar(registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                UPDATE registro_tiempo 
                SET fecha = {marca}, horas = {marca}, descripcion = {marca}, 
                    empleado_id = {marca}, proyecto_id = {marca}
                WHERE id = {marca}
            """
            cursor.execute(
                sql,
                (
                    registro.fecha,
                    registro.horas,
                    registro.descripcion,
                    registro.empleado_id,
                    registro.proyecto_id,
                    registro.id
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
            SELECT id, fecha, horas, descripcion, empleado_id, proyecto_id 
            FROM registro_tiempo
        """)
        filas = cursor.fetchall()
        conexion.close()
        
        registros = []
        for fila in filas:
            registros.append(RegistroTiempoDAO._fila_a_registro(fila))
            
        return registros

    @staticmethod
    def _fila_a_registro(fila):
        # Transforma el registro devuelto por la BD en un objeto RegistroTiempo
        return RegistroTiempo(
            id=fila[0],
            fecha=fila[1],
            horas=fila[2],
            descripcion=fila[3],
            empleado_id=fila[4],
            proyecto_id=fila[5]
        )