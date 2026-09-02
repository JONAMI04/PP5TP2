from ItemDeTrabajo import ItemDeTrabajo

class OrdenDeTrabajo:
    def __init__(self, numero, vehiculo, mecanico):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("El número de orden debe ser un entero positivo.")
        self.numero = numero
        self.vehiculo = vehiculo

        self.mecanico = mecanico
        self._item_de_trabajo = []

    def agregar_item_de_trabajo(self, item):
        if not isinstance(item, ItemDeTrabajo):
            raise ValueError("El item debe ser una instancia de la clase ItemDeTrabajo.")
        if not item.esta_disponible():
            raise Exception(f"El item {item.nombre} no está disponible para ser agregado a la orden de trabajo.")
        item.asignar_item()
        self._item_de_trabajo.append(item)

    def calcular_total(self):
        total = sum(item.precio * item.cantidad for item in self._item_de_trabajo)
        return total

    def asignar_mecanico(self, mecanico):
        if not mecanico.esta_libre():
            raise Exception(f"El mecánico {mecanico.nombre} no está disponible para ser asignado a la orden de trabajo.")
        mecanico.dar_trabajo()
        self.mecanico = mecanico

    def asignar_vehiculo(self, vehiculo):
        if not vehiculo.esta_disponible():
            raise Exception(f"El vehículo con dominio {vehiculo.dominio} no está disponible para ser asignado a la orden de trabajo.")
        self.vehiculo = vehiculo