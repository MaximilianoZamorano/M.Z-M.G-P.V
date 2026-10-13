import os
import sqlite3
import pymysql
from dotenv import load_dotenv
load_dotenv()

def obtener_motor():
    return os.getenv("DB_ENGINE", "sqlite").lower()

def abrir_conexion():
    motor = obtener_motor() 
    
    if motor == "sqlite":
        # Obtiene el nombre del archivo desde el .env o usa el default
        nombre_db = os.getenv("DB_NAME", "ecotech.db")
        
        # Obtiene la ruta absoluta de la carpeta donde está ESTE archivo (conexion.py)
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        
        # Une la ruta con el nombre de la base de datos
        ruta_absoluta = os.path.join(directorio_actual, nombre_db)
        
        return sqlite3.connect(ruta_absoluta)
    
    if motor == "mysql":
        return pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3307")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            charset="utf8mb4"
        )
        
    raise ValueError(f"Motor no soportado: {motor}")

# persistencia/conexion.py
def marcador_sql():
    if obtener_motor() == "sqlite":
        return "?"
    return "%s"