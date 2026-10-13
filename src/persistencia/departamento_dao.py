from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.departamento import Departamento

class DepartamentoDAO:
    @staticmethod
    def insertar(departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            INSERT INTO departamento (nombre, gerente_id)
            VALUES ({marca}, {marca})
        """
        # Obtenemos el id del gerente si está asignado en el objeto
        gerente_id = getattr(departamento, 'gerente_id', None)
        
        cursor.execute(sql, (departamento.nombre, gerente_id))
        departamento.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return departamento
    
    @staticmethod
    def eliminar(id_departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"DELETE FROM departamento WHERE id = {marca}"
        cursor.execute(sql, (id_departamento,))
        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado

    @staticmethod
    def obtenerPorId(id_departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            SELECT id, nombre, gerente_id
            FROM departamento WHERE id = {marca}
        """
        cursor.execute(sql, (id_departamento,))
        fila = cursor.fetchone()
        conexion.close()
        
        if fila is None:
            return None
        
        return DepartamentoDAO._fila_a_departamento(fila)

    @staticmethod
    def actualizar(departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                UPDATE departamento 
                SET nombre = {marca}, gerente_id = {marca}
                WHERE id = {marca}
            """
            gerente_id = getattr(departamento, 'gerente_id', None)
            
            cursor.execute(
                sql,
                (
                    departamento.nombre,
                    gerente_id,
                    departamento.id
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
        cursor.execute("SELECT id, nombre, gerente_id FROM departamento")
        filas = cursor.fetchall()
        conexion.close()
        
        departamentos = []
        for fila in filas:
            departamentos.append(DepartamentoDAO._fila_a_departamento(fila))
            
        return departamentos

    @staticmethod
    def _fila_a_departamento(fila):
        # Mapea los datos retornados por la BD al objeto Departamento
        # Instancia Departamento(nombre, gerente_id, id) segun tu definicion de dominio
        dep = Departamento(nombre=fila[1], id=fila[0])
        if hasattr(dep, 'gerente_id'):
            dep.gerente_id = fila[2]
        return dep