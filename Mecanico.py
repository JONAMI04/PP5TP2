class Mecanico:
    def __init__(self, nombre, lagajo):
        self.nombre = nombre
        self.lagajo = lagajo

        self._disponible = True

    def esta_libre(self):
        if not self._disponible:
            raise Exception(f"El mecánico {self.nombre} no está disponible.")
        return self._disponible

    def dar_trabajo(self):
        if self.esta_libre():
            self._disponible = False