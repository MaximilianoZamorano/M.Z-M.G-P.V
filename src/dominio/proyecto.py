from typing import Optional, List

class Proyecto:
    def __init__(self, nombre: str, descripcion: str, fechaInicio: str, id: Optional[int] = None):
        # El ID se pone como opcional y al final para facilitar la creación antes de guardarlo en la BD
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio # En el diagrama es tipo date (se puede usar str o datetime.date)
        
        # Lista para almacenar objetos RegistroTiempo
        self._registros_horas = [] 
    
    # Nombre de función ajustado al camelCase del diagrama UML
    def agregarRegistro(self, r):
        self._registros_horas.append(r)

    # Método requerido por el diagrama de clases
    def calcularHorasTotales(self) -> float:
        total = 0.0
        for registro in self._registros_horas:
            # Asume que los objetos en la lista tienen un atributo 'horas'
            total += registro.horas
        return total