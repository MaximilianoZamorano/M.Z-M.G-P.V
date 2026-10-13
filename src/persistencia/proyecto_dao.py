from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.proyecto import Proyecto 

class ProyectoDAO:
    @staticmethod
    def insertar(proyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            INSERT INTO proyecto (nombre, descripcion, fecha_inicio)
            VALUES ({marca}, {marca}, {marca})
        """
        cursor.execute(sql, (
            proyecto.nombre, 
            proyecto.descripcion, 
            proyecto.fechaInicio
        ))
        proyecto.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return proyecto
    
    @staticmethod
    def eliminar(id_proyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"DELETE FROM proyecto WHERE id = {marca}"
        cursor.execute(sql, (id_proyecto,))
        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado

    @staticmethod
    def obtenerPorId(id_proyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            SELECT id, nombre, descripcion, fecha_inicio
            FROM proyecto WHERE id = {marca}
        """
        cursor.execute(sql, (id_proyecto,))
        fila = cursor.fetchone()
        conexion.close()
        
        if fila is None:
            return None
        
        return ProyectoDAO._fila_a_proyecto(fila)

    @staticmethod
    def actualizar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                UPDATE proyecto 
                SET nombre = {marca}, descripcion = {marca}, fecha_inicio = {marca}
                WHERE id = {marca}
            """
            cursor.execute(
                sql,
                (
                    proyecto.nombre,
                    proyecto.descripcion,
                    proyecto.fechaInicio,
                    proyecto.id
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
        cursor.execute("SELECT id, nombre, descripcion, fecha_inicio FROM proyecto")
        filas = cursor.fetchall()
        conexion.close()
        
        proyectos = []
        for fila in filas:
            proyectos.append(ProyectoDAO._fila_a_proyecto(fila))
            
        return proyectos

    @staticmethod
    def _fila_a_proyecto(fila):
        # Transforma el registro devuelto por la BD en un objeto Proyecto
        return Proyecto(
            id=fila[0],
            nombre=fila[1],
            descripcion=fila[2],
            fechaInicio=fila[3]
        )