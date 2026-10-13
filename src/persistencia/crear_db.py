from persistencia.conexion import abrir_conexion, obtener_motor

def crear_tablas():
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    
    if obtener_motor() == "sqlite":
        # === SINTAXIS PARA SQLITE ===
        
        sql_departamento = '''
            CREATE TABLE IF NOT EXISTS departamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                gerente_id INTEGER
            )
        '''
        
        sql_proyecto = '''
            CREATE TABLE IF NOT EXISTS proyecto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                fecha_inicio DATE
            )
        '''
        
        # Atributos actualizados según el diagrama de clases
        sql_empleado = '''
            CREATE TABLE IF NOT EXISTS empleado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                direccion TEXT,
                telefono TEXT,
                email TEXT NOT NULL,
                fechaInicioContrato DATE,
                salario REAL,
                departamento_id INTEGER,
                FOREIGN KEY (departamento_id) REFERENCES departamento(id)
            )
        '''
        
        sql_registro_tiempo = '''
            CREATE TABLE IF NOT EXISTS registro_tiempo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha DATE NOT NULL,
                horas REAL NOT NULL,
                descripcion TEXT,
                empleado_id INTEGER NOT NULL,
                proyecto_id INTEGER NOT NULL,
                FOREIGN KEY (empleado_id) REFERENCES empleado(id),
                FOREIGN KEY (proyecto_id) REFERENCES proyecto(id)
            )
        '''
        
    else:
        # === SINTAXIS PARA MYSQL (PYMYSQL) ===
        
        sql_departamento = '''
            CREATE TABLE IF NOT EXISTS departamento (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL,
                gerente_id INT
            )
        '''
        
        sql_proyecto = '''
            CREATE TABLE IF NOT EXISTS proyecto (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL,
                descripcion TEXT,
                fecha_inicio DATE
            )
        '''
        
        # Atributos actualizados según el diagrama de clases
        sql_empleado = '''
            CREATE TABLE IF NOT EXISTS empleado (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL,
                direccion VARCHAR(200),
                telefono VARCHAR(20),
                email VARCHAR(150) NOT NULL,
                fechaInicioContrato DATE,
                salario FLOAT,
                departamento_id INT,
                FOREIGN KEY (departamento_id) REFERENCES departamento(id)
            )
        '''
        
        sql_registro_tiempo = '''
            CREATE TABLE IF NOT EXISTS registro_tiempo (
                id INT PRIMARY KEY AUTO_INCREMENT,
                fecha DATE NOT NULL,
                horas FLOAT NOT NULL,
                descripcion TEXT,
                empleado_id INT NOT NULL,
                proyecto_id INT NOT NULL,
                FOREIGN KEY (empleado_id) REFERENCES empleado(id),
                FOREIGN KEY (proyecto_id) REFERENCES proyecto(id)
            )
        '''

    # Ejecutar las consultas en orden para respetar las dependencias (Claves Foráneas)
    cursor.execute(sql_departamento)
    cursor.execute(sql_proyecto)
    cursor.execute(sql_empleado)
    cursor.execute(sql_registro_tiempo)

    conexion.commit()
    conexion.close()

crear_tablas()
