class Proyecto:
    def __init__(self, id: int, nombre: str, descripcion: str, fechaInicio: int):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio
        self.registro_horas = []
    
    def agregar_registro(self,registro):
        self.registros_horas.append(registro)
