from Taller import Taller
from Mecanico import Mecanico
from OrdenDeTrabajo import OrdenDeTrabajo
from ItemDeTrabajo import ItemDeTrabajo

from Vehiculo import Vehiculo

taller = Taller("taller feliz")
taller2 = Taller("taller rechazo")
taller3 = Taller("taller 3")

mecanico1 = Mecanico("Juan", "123")
mecanico2 = Mecanico("Pedro", "456")
mecanico3 = Mecanico("Jose", "789")

vehiculo1 = Vehiculo("ABC123")
vehiculo2 = Vehiculo("KEV123")
vehiculo3 = Vehiculo("XYZ789")

orden1 = OrdenDeTrabajo(1, vehiculo1, mecanico1)
orden2 = OrdenDeTrabajo(2, vehiculo2, mecanico2)


taller.agregar_mecanico(mecanico1)
taller.agregar_orden_de_trabajo(orden1)

item1 = ItemDeTrabajo("Cambio de aceite", 1000, 1)
orden1.agregar_item_de_trabajo(item1)
orden2.agregar_item_de_trabajo(item1)
print(orden1.calcular_total())

taller.quitar_mecanicos(mecanico1)

