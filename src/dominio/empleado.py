from dominio.registroTiempo import RegistroTiempo

class Empleado:
    def __init__(self, nombre: str, correo: str, telefono: int, id=None):
        self.nombre = nombre
        self.correo = correo
        self._registroTiempo: list[RegistroTiempo] = []
        self.telefono = telefono
        self.id = id

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.correo} - {self.telefono}"

    def agregar_tiempo(self, fecha: str, horas: float) -> bool:
        return True

