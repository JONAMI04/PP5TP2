from Mecanico import Mecanico
from OrdenDeTrabajo import OrdenDeTrabajo

class Taller:
    def __init__(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del taller no puede estar vacío.")
        self.nombre = nombre
        self._ordenes_de_trabajo = []
        self._mecanicos = []

    def agregar_mecanico(self, mecanico):
        if not isinstance(mecanico, Mecanico):
            raise ValueError("Debe ser un Mecanico.")
        self._mecanicos.append(mecanico)

    def quitar_mecanicos(self, mecanico):
        if mecanico in self._mecanicos:
            self._mecanicos.remove(mecanico)
        else:
            raise ValueError("El mecánico no se encuentra en el plantilla del taller.")

    def agregar_orden_de_trabajo(self, orden):
        if not isinstance(orden, OrdenDeTrabajo):
            raise ValueError("Debe ser una OrdenDeTrabajo.")
        self._ordenes_de_trabajo.append(orden)