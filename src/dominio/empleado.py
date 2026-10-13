from dominio.registro_tiempo import RegistroTiempo
from datetime import date

class Empleado:
    def __init__(self, nombre: str, direccion: str, telefono: str, email: str, 
                 fechaInicioContrato: date, salario: float, departamento_id: int = None, id: int = None):
        # Atributos basados en el diagrama de clases y la base de datos
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fechaInicioContrato = fechaInicioContrato
        self.salario = salario
        self.departamento_id = departamento_id
        
        # Lista para la relación con los registros de tiempo
        self._registroTiempo = [] 

    def mostrar_datos(self) -> str:
        # Se actualizó para mostrar la nueva información
        return f"{self.nombre} - {self.email} - {self.telefono} - ${self.salario}"

    # Nuevos métodos requeridos por el diagrama UML
    def actualizarDatos(self, nombre: str = None, direccion: str = None, 
                        telefono: str = None, email: str = None, salario: float = None):
        if nombre: self.nombre = nombre
        if direccion: self.direccion = direccion
        if telefono: self.telefono = telefono
        if email: self.email = email
        if salario: self.salario = salario

    def asignarDepartamento(self, id_departamento: int):
        self.departamento_id = id_departamento

    def agregar_tiempo(self, fecha: str, horas: float) -> bool:
        # Aquí iría la lógica para agregar objetos RegistroTiempo a self._registroTiempo
        return True

