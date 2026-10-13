from typing import Optional, List
from dominio.empleado import Empleado

class Departamento:
    def __init__(self, nombre: str, gerente: Optional[Empleado] = None, id: Optional[int] = None):
        self.id = id
        self.nombre = nombre
        self.gerente = gerente
        self._empleados: List[Empleado] = []

    def asignarGerente(self, e: Empleado):
        self.gerente = e

    def agregarEmpleado(self, e: Empleado) -> bool:
        if e not in self._empleados:
            self._empleados.append(e)
            if hasattr(e, 'asignarDepartamento') and self.id is not None:
                e.asignarDepartamento(self.id)
            return True
        return False

    def quitarEmpleado(self, e: Empleado) -> bool:
        if e in self._empleados:
            self._empleados.remove(e)
            return True
        return False

    @property
    def empleados(self) -> tuple:
        return tuple(self._empleados)

    def cantidad_empleados(self) -> int:
        return len(self._empleados)