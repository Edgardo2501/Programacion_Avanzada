# Instanciacion del modelo de cafeteria
from modelo_cafeteria import *

# Utilizamos la siguiente nuneracion para los ID de los objetos:
# - Clientes: 1 a 10
# - Empleados: 11 a 20
# - Bebidas: 101 a 110
# - Postres: 201 a 210
# - Pedidos: 1001 a 1010

# creamos una lista de 10 objetos de la clase 'Cliente'
clientes = [
    Cliente(1, "Ana Martinez", "ana@mail.com", 50),
    Cliente(2, "Luis Gomez", "luis@mail.com", 120),
    Cliente(3, "Carlos Perez", "carlos@mail.com", 0),
    Cliente(4, "Maria Lopez", "maria@mail.com", 30),
    Cliente(5, "Sofia Diaz", "sofia@mail.com", 200),
    Cliente(6, "Jorge Ruiz", "jorge@mail.com", 15),
    Cliente(7, "Elena Torres", "elena@mail.com", 80),
    Cliente(8, "Pedro Sanchez", "pedro@mail.com", 45),
    Cliente(9, "Lucia Ramirez", "lucia@mail.com", 90),
    Cliente(10, "Raul Castro", "raul@mail.com", 110)
]

# creamos una lista de 10 objetos de la clase 'Empleado'
empleados = [
    Empleado(11, "Roberto", "rob@cafe.com", "E001", Rol.GERENTE),
    Empleado(12, "Diana", "dia@cafe.com", "E002", Rol.BARISTA),
    Empleado(13, "Fernando", "fer@cafe.com", "E003", Rol.MESERO),
    Empleado(14, "Carmen", "car@cafe.com", "E004", Rol.BARISTA),
    Empleado(15, "Hugo", "hugo@cafe.com", "E005", Rol.MESERO),
    Empleado(16, "Marta", "mar@cafe.com", "E006", Rol.BARISTA),
    Empleado(17, "Diego", "die@cafe.com", "E007", Rol.MESERO),
    Empleado(18, "Laura", "lau@cafe.com", "E008", Rol.MESERO),
    Empleado(19, "Oscar", "osc@cafe.com", "E009", Rol.BARISTA),
    Empleado(20, "Patricia", "pat@cafe.com", "E010", Rol.BARISTA)
]

# creamos una lista de 10 objetos de la clase 'Bebida'
bebidas = [
    Bebida(101, "Americano", 35.0, "Mediano", Temperatura.CALIENTE),
    Bebida(102, "Capuchino", 45.0, "Grande", Temperatura.CALIENTE),
    Bebida(103, "Latte Frio", 50.0, "Grande", Temperatura.FRIA),
    Bebida(104, "Espresso", 30.0, "Chico", Temperatura.CALIENTE),
    Bebida(105, "Frappe Moka", 60.0, "Grande", Temperatura.FRIA),
    Bebida(106, "Te Verde", 40.0, "Mediano", Temperatura.CALIENTE),
    Bebida(107, "Te Helado", 45.0, "Grande", Temperatura.FRIA),
    Bebida(108, "Macchiato", 40.0, "Chico", Temperatura.CALIENTE),
    Bebida(109, "Chocolate", 55.0, "Mediano", Temperatura.CALIENTE),
    Bebida(110, "Smoothie Fresa", 65.0, "Grande", Temperatura.FRIA)
]

# creamos una lista de 10 objetos de la clase 'Postre'
postres = [
    Postre(201, "Pastel de Zanahoria", 50.0, True, False),
    Postre(202, "Brownie", 40.0, False, False),
    Postre(203, "Galleta de Avena", 25.0, True, True),
    Postre(204, "Cheesecake", 60.0, False, False),
    Postre(205, "Muffin de Arandano", 35.0, False, False),
    Postre(206, "Tarta de Manzana", 45.0, True, False),
    Postre(207, "Panque de Nuez", 40.0, False, False),
    Postre(208, "Macarons", 55.0, False, True),
    Postre(209, "Trufas de Chocolate", 30.0, True, True),
    Postre(210, "Croissant", 35.0, False, False)
]

# creamos una lista de 10 objetos de la clase 'Pedido'
pedidos = [Pedido(i) for i in range(1001, 1011)]

# creamos la instancia unica de Inventario para el control general
inventario_central = Inventario()
inventario_central.ingredientes = {"cafe": 1000, "leche": 500, "azucar": 300}

# Imprimir listas de objetos para verificacion
print("Lista de clientes:")
for c in clientes:
    print(c)

print("Lista de empleados:")
for e in empleados:
    print(e)

print("Menu de bebidad")
for b in bebidas:
    print(b)

print("Menu de postres")
for p in postres:
    print(p)

# Probamos el sistema con una simulacion de pedido, aplicando un descuento promocional y validando el inventario.
print("SIMULACION DE PEDIDO")

# Seleccionamos un cliente, un barista y productos
cliente_actual = clientes[0]
barista_actual = empleados[1]
bebida_elegida = bebidas[1] # Capuchino
postre_elegido = postres[0] # Pastel de Zanahoria

print(f"Atendiendo a: {cliente_actual.nombre}")
print(f"Barista en turno: {barista_actual.nombre}")

# Modificando la bebida modificadores
bebida_elegida.agregar_extra("Leche de almendra", 10.0)
bebida_elegida.agregar_extra("Sin azucar", 0.0)

# Armado del pedido
pedido_actual = pedidos[0]
pedido_actual.agregar_producto(bebida_elegida)
pedido_actual.agregar_producto(postre_elegido)
pedido_actual.calcular_total()

# Realizamos el pedido y cambiamos su estado
cliente_actual.realizar_pedido(pedido_actual)
barista_actual.cambiar_estado_pedido(pedido_actual, Estado.PREPARANDO)

# Mostrar resultados
print("Sistema: Resumen del Pedido")
print(pedido_actual)
print(f"Puntos de fidelidad de {cliente_actual.nombre}: {cliente_actual.puntosFidelidad}")

# Comprobando el inventario
print("Sistema: Actualizando inventario")
barista_actual.actualizar_inventario(inventario_central, "leche_almendra", 50)
inventario_central.reducir_inventario("cafe", 20)
print(f"Inventario de cafe restante: {inventario_central.ingredientes['cafe']}")