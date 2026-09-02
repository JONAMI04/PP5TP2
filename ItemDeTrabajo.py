class ItemDeTrabajo:

    def __init__(self, nombre, precio, cantidad):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del item no puede estar vacío.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self._disponible = True

    def esta_disponible(self):
        if not self._disponible:
            raise Exception(f"El item {self.nombre} no está disponible.")
        return self._disponible

    def asignar_item(self):
        if self.esta_disponible():
            self._disponible = False