# Creación de las siguientes clases:
# 1. Pelicula
# Atributos: nombre, genero, duracion
# Métodos: mostrar detalles
# 2. Producto
# Atributos: id, nombre, precio, categoria
# 3. Usuario
# Atributos: id, nombre, puntos


# Clase 'pelicula'
class pelicula:
    def __init__(self, nombre, genero, duracion):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
    def mostrar_detalles(self):
        return f"Película: {self.nombre}, Género: {self.genero}, Duración: {self.duracion} minutos"
        

# Clase 'producto'
class producto:
    def __init__(self, id, nombre, precio, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        
    def __str__(self):
        return f"ID: {self.id}, {self.nombre}, (${self.precio}), Categoría: {self.categoria}"

# Clase 'usuario'
class usuario:
    def __init__(self, id, nombre, puntos):
        self.id = id
        self.nombre = nombre
        self.puntos = puntos
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Puntos: {self.puntos}"
    
