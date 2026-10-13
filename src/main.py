from persistencia.crear_db import crear_tablas
from presentacion.menu_principal import iniciar_menu_principal

def main():
    # 1. Inicializa la base de datos y las tablas si no existen
    crear_tablas() 
    
    # 2. Inicia el flujo interactivo del programa
    iniciar_menu_principal()

if __name__ == "__main__":
    main()


