Conceptos en el dominio:
Taller, Vehículo, Orden de Trabajo, Visita, Ítem de Trabajo, Mano de Obra, Repuesto, Mecánico, Plantilla de Mecánicos, Presupuesto.

No se convierten en clases:
Presupuesto
ya que es un valor derivado, no requiere almacenar sino que vasta con calcularlo de los items de trabajo en de la orden de trabajo en tiempo de ejecución sumando el costo unitario por cantidad de cada item. 

Visita
Cada vez que un auto ingresa al taller es una visita, y por ende se genera una Orden de trabajo. La visita queda registrada mediante la fecha de de la Orden de trabajo.

Plantilla de Mecánicos
La plantilla es el listado de Mecánicos.

Mano de Obra o Repuesto
Son items necesarios pero algoritmos de cálculo de precio seria similar, cantidad de horas o cantidad de repuestos por el valor unitario. por lo tanto no justifican ser clases.


Tarjetas CRC:

Clase: Taller
Responsabilidades: Asignar un mecánico a una orden de trabajo, Asignar un vehículo a una orden de trabajo.
Colaboradores: Vehículo, Mecánico, OrdenDeTrabajo


Clase: OrdenDeTrabajo	
Responsabilidades: Conocer el estado actual de la orden, Mantener la referencia al vehículo asociado a la orden, Mantener la referencia al mecánico asignado, Contener y gestionar la lista de ítems agregados durante la revisión, Calcular el monto total.
Colaboradores: Vehículo, Mecánico, ItemDeTrabajo

Clase: Vehículo	
Responsabilidades: Mantener e identificar sus datos, Validar la identificación del vehículo
Colaboradores: Ninguno

Clase: Mecánico	
Responsabilidades: Mantener la información del mecánico, Conocer y actualizar su estado.
Colaboradores: Ninguno

Clase: ItemDeTrabajo
Responsabilidades: Mantener la descripción y el precio del ítem
Colaboradores: Ninguno	

OrdenDeTrabajo – ItemDeTrabajo
Es Composición porque es un todo, donde el ciclo de vida del ItemDeTrabajo está junto al de la OrdenDeTrabajo. Un ítem de trabajo no puede existir fuera de la orden. Si la OrdenDeTrabajo se elimina todos los ItemDeTrabajo se eliminan con ella.
No es Agregación porque las partes podrian existir independientemente.
No es Asociación porque esstan describen un vínculo entre dos objetos independientes. 
No es Dependencia porque la Orden de trabajo mantiene una lista de sus ítems almacenada en sus atributos. La dependencia implica solo un uso temporal, mientras que aquí hay una estructura fija que perdura en el tiempo.

Taller – Mecanico
Es Agregación, porque el Taller agrupa a la plantilla de Mecanico, pero sus ciclos de vida son independientes. Si el Taller se destruye, el Mecánico sigue existiendo y puede ser reasignado a otro taller.
No es Composición, porque destruir el contenedor destruye a sus componentes. Eliminar la instancia de Taller no destruye al Mecánico.
NO es Asociación, porque el taller tiene una lista de mecánicos.
NO es Dependencia, porque el taller conserva a los mecánicos mediante una referencia.

OrdenDeTrabajo – Vehiculo
Es Asociación, porueq Es un vínculo entre dos entidades independientes que colaboran. Ambas clases poseen ciclos de vida independientes y no son partes de la otra.
NO es Agregación, porque la orden de trabajo no contiene al vehículo, ni el vehículo es integra la orden.
NO es Composición, porque Si la Orden de trabajo se elimina, el Vehículo existiendo.
NO es Dependencia, porqeu la Orden de trabajo guarda la referencia al Vehículo. no es una relación espontanea

Cálculo del Presupuesto
Es Dependencia ya que la relación es espontanea se calcula y luego termina la realacion con las demás clases.
NO es Asociación, porque no existe un atributo duradero que guarde el cálculo, se invoca, procesa los datos y devuelve un valor.
NO es Agregación ni Composición: El cálculo no es una parte de nada.