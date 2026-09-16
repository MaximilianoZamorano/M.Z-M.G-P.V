from dominio.proyecto import Proyecto

class RegistroTiempo:
    def __init__(self, id: int, proyecto: Proyecto, horas: float, detalle: str, fecha: str):
        self.id = id
        self.proyecto = proyecto
        self.horas = horas
        self.detalle = detalle
        self.fecha = fecha

    def mostrar_tiempo(self) -> str:
        return f"{self.fecha} - {self.horas}horas"

