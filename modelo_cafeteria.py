# Modelo de Cafeteria
# Este modelo incluye clases para Clientes, Empleados, Productos (Bebidas y Postres), 
# pedidos e Inventario, junto con enumeraciones para roles, temperaturas y estados de pedidos

# importamos las herramientas necesarias
from abc import ABC, abstractmethod # para las clases abstracta
from enum import Enum # para las enumeraciones

# Definimos las enumeraciones
class Rol(Enum):
    BARISTA = "Barista"
    MESERO = "Mesero"
    GERENTE = "Gerente"

class Temperatura(Enum):
    FRIA = "Fría"
    CALIENTE = "Caliente"

class Estado(Enum):
    PENDIENTE = "Pendiente"
    PREPARANDO = "Preparando"
    ENTREGADO = "Entregado"

# MODULO 1: PERSONAS

# Definimos la clase base abstracta 'Persona'
class Persona(ABC):
    # atributos
    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
    # metodo: login 
    def login(self):
        return f"Bienvenido de nuevo, {self.nombre} ha iniciado sesion."
    # metodo: actualizar perfil
    def actualizar_perfil(self, nuevo_email):
        self.email = nuevo_email
        return "Perfil actualizado correctamente"

# Definimos la clase 'Cliente'
class Cliente(Persona):
    # atributos
    def __init__(self, idPersona, nombre, email, puntosFidelidad):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad = puntosFidelidad
        self.historialPedidos = []
    # metodo: realizar pedido
    def realizar_pedido(self, pedido):
        self.historialPedidos.append(pedido)
        self.puntosFidelidad += 10
        return f"el Pedido se ha realizado. Puntos actuales: {self.puntosFidelidad}"
    # metodo: consultar historial de pedidos
    def consultar_historial(self):
        return self.historialPedidos
    # metodo: canjear puntos
    def canjear_puntos(self, puntos_a_canjear):
        if self.puntosFidelidad >= puntos_a_canjear:
            self.puntosFidelidad -= puntos_a_canjear
            return True
        return False

    def __str__(self):
        return f"Cliente ID: {self.idPersona}, Nombre: {self.nombre}, Puntos: {self.puntosFidelidad}"

# definimos la clase 'Empleado'
class Empleado(Persona):
    # atributos
    def __init__(self, idPersona, nombre, email, idEmpleado, rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado = idEmpleado
        self.rol = rol
    # meodo: actualizar inventario
    def actualizar_inventario(self, inventario, ingrediente, cantidad):
        inventario.ingredientes[ingrediente] = inventario.ingredientes.get(ingrediente, 0) + cantidad
        return f"el Inventario se ha actualizado. {ingrediente}: {inventario.ingredientes[ingrediente]}"
    # método: cambiar estado de pedido
    def cambiar_estado_pedido(self, pedido, estado_nuevo):
        pedido.estado = estado_nuevo
        return f"Estado del pedido {pedido.idPedido} cambiado a {estado_nuevo.value}"

    def __str__(self):
        return f"Empleado ID: {self.idEmpleado}, Nombre: {self.nombre}, Rol: {self.rol.value}"

# Creamos el Modulo de Productos

# Definimos la clase base 'ProductoBase'
class ProductoBase:
    # atributos
    def __init__(self, id_Producto, nombre, precioBase):
        self.idProducto = id_Producto
        self.nombre = nombre
        self.precioBase = precioBase

# Definimos la clase 'Bebida'
class Bebida(ProductoBase):
    # atributos
    def __init__(self, id_Producto, nombre, precioBase, medida, temperatura):
        super().__init__(id_Producto, nombre, precioBase)
        self.medida = medida
        self.temperatura = temperatura
        self.modificadores = []
    # metodo: agregar modificador a la bebida
    def agregar_extra(self, modificador, precio_con_mod):
        self.modificadores.append({"nombre": modificador, "precio": precio_con_mod})
    # metodo: calcular precio final de la bebida con modificadores
    def calcular_precio_final(self):
        precio_modificadores = sum(mod["precio"] for mod in self.modificadores)
        return self.precioBase + precio_modificadores

    def __str__(self):
        return f"Bebida: {self.nombre} ({self.medida}, {self.temperatura.value}) - ${self.precioBase}"

# definimos la clase 'Postre'
class Postre(ProductoBase):
    # atributos
    def __init__(self, id_Producto, nombre, precioBase, esVegano, sinGluten):
        super().__init__(id_Producto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten = sinGluten

    def __str__(self):
        v = "Vegano" if self.esVegano else "Normal"
        g = "Sin Gluten" if self.sinGluten else "Con Gluten"
        return f"Postre: {self.nombre} [{v}, {g}] - ${self.precioBase}"

# Creamos el modulo 3: Logistica y ventas

# DEfinimos la clase 'Inventario'
class Inventario:
    def __init__(self):
        self.ingredientes = {}
    # metodo: reducir inventario de un ingrediente
    def reducir_inventario(self, ingrediente, cantidad):
        if self.ingredientes.get(ingrediente, 0) >= cantidad:
            self.ingredientes[ingrediente] -= cantidad
            return True
        else:
            self.notificar_faltante(ingrediente)
            return False
    # metodo: notificar faltante de un ingrediente
    def notificar_faltante(self, ingrediente):
        print(f"[error]: No hay inventario suficiente de {ingrediente}")

# Definimos la clase 'Pedido'
class Pedido:
    # atributos
    def __init__(self, idPedido):
        self.idPedido = idPedido
        self.productos = []
        self.estado = Estado.PENDIENTE
        self.total = 0.0
    # metodo: agregar producto al pedido
    def agregar_producto(self, producto):
        self.productos.append(producto)
    # metodo: calcular total del pedido
    def calcular_total(self):
        total_temp = 0.0
        for prod in self.productos:
            if isinstance(prod, Bebida):
                total_temp += prod.calcular_precio_final()
            else:
                total_temp += prod.precioBase
        self.total = total_temp
        return self.total
    # metodo: validar inventario de los productos en el pedido
    def validar_stock(self, inventario):
        return len(self.productos) > 0

    def __str__(self):
        nombres_productos = [p.nombre for p in self.productos]
        return f"Pedido n°{self.idPedido}, Estado: {self.estado.value}, Productos: {nombres_productos}, Total: ${self.total:.2f}"