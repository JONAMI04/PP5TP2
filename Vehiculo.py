class Vehiculo:
    def __init__(self, dominio):
        if not dominio or not dominio.strip():

            raise ValueError("El dominio no puede estar vacío.")
        self.dominio = dominio
        self._disponible = True

    def esta_disponible(self):
        if not self._disponible:
            raise Exception(f"El vehículo con dominio {self.dominio} no está disponible.")
        return True

    def arreglando(self):
        if self.esta_disponible():
            self._disponible = False