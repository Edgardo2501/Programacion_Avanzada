from models_cine import pelicula, producto, usuario

# 10 objetos de cada clase
# Objetos de la clase 'pelicula'
peliculas = [
    pelicula("Inception", "Sci-Fi", 148),
    pelicula("Mommy", "Drama", 152),
    pelicula("Pulp Fiction", "Crimen", 154),
    pelicula("Avatar", "Aventura", 162),
    pelicula("Toy Story", "Animación", 81),
    pelicula("The Matrix", "Sci-Fi", 136),
    pelicula("Gladiator", "Drama", 155),
    pelicula("Jurassic Park", "Aventura", 127),
    pelicula("Coco", "Animación", 105),
    pelicula("Avengers: Endgame", "Acción", 181)]
# Objetos de la clase 'producto'
productos = [
    producto(1, "Palomitas Grandes", 8.50, "Snacks"),
    producto(2, "Refresco Mediano", 4.00, "Bebidas"),
    producto(3, "Hot Dog", 5.50, "Comida"),
    producto(4, "Nachos con Queso", 6.00, "Snacks"),
    producto(5, "Dulces", 3.00, "Snacks"),
    producto(6, "Agua Embotellada", 2.50, "Bebidas"),
    producto(7, "Combo Pareja", 15.00, "Combos"),
    producto(8, "Chocolate", 3.50, "Snacks"),
    producto(9, "Té Helado", 4.50, "Bebidas"),
    producto(10, "Palomitas de Caramelo", 9.00, "Snacks")
]
# Objetos de la clase 'usuario'
usuarios = [
    usuario(101, "Edgar", 120),
    usuario(102, "Maria", 150),
    usuario(103, "Juan", 90),
    usuario(104, "Ana", 200),
    usuario(105, "Luis", 80),
    usuario(106, "Sofia", 170),
    usuario(107, "Carlos", 110),
    usuario(108, "Laura", 130),
    usuario(109, "Diego", 95),
    usuario(110, "Marta", 160)
]

# Utilizamos el ciclo for para mostrar los detalles de cada película
print("Detalles de las películas:")
for p in peliculas:
    print(p.mostrar_detalles())

# Utilizamos el ciclo for para mostrar los detalles de cada producto
print("Detalles de los productos:")
for pr in productos:
    print(pr)

# Utilizamos el ciclo for para mostrar los detalles de cada usuario
print("Detalles de los usuarios:")
for u in usuarios:
    print(u)

# Funciones para cumplir con los retos.
asientos_ocupados = ["A2", "C1", "D4"]  

# Definimos la función para validar un descuento promocional
def aplicar_descuento(monto_base):
    print("Aplicando promocion")
    codigo_promocional = input("¿Cuenta con algún código de promoción? (SI/NO): ").upper()
    
    if codigo_promocional == "SI":
        codigo = input("Código: ")
        if codigo == "ESTUDIANTE_BUAP":
            descuento = monto_base * 0.10
            total = monto_base - descuento
            print("[SISTEMA]: Espere un momento, estamos validando el codigo. Código válido, el descuento se ha aplicado con exito.")
            return total, descuento
        else:
            print("[SISTEMA]: Código inválido.")
    
    return monto_base, 0

# Realizamos el flujo de reserva de la película.
print("Reservando asientos")


cliente = usuarios[0] 
pelicula_seleccionada = peliculas[0]
print(f"Usuario: {cliente.nombre} (Puntos disponibles: {cliente.puntos})")
print(f"Función {pelicula_seleccionada.mostrar_detalles()}")

# usamos ciclo while para validar la selección de asientos
while True:
    seleccion = input("Seleccione sus asientos (separados por coma): ")
    # Convertimos la entrada "A1, A2" en una lista ["A1", "A2"] limpia y sin espacio en blanco
    asientos_pedidos = [a.strip().upper() for a in seleccion.split(",")] # nota: strip nos sirve para eliminar espacios en blanco al inicio o final de cada asiento
    
    print("[SISTEMA]: Estamos validando la disponibilidad de los asientos seleccionados")
    ocupados = False
    
    for asiento in asientos_pedidos:
        if asiento in asientos_ocupados:
            print(f"[ERROR]: El asiento {asiento} ya está ocupado por la Reserva #999.")
            ocupados = True
            break
            
    if not ocupados:
        print(f"[OK]: Asientos {', '.join(asientos_pedidos)} han sido elegidos con éxito.")
        break # usamos break para salir del ciclo while una vez que se han seleccionado asientos disponibles
    else:
        print("[SISTEMA]: Por favor, seleccione asientos disponibles.")

# Cálculo 
monto_inicial = len(asientos_pedidos) * 140.00
print(f"Monto base: ${monto_inicial:.2f}")

# Proceso de pago y descuento
monto_final, ahorro = aplicar_descuento(monto_inicial)

# Resumen finall
print(f"Resumen de Reserva N°999:")
print(f"Usuario: {cliente.nombre}")
print(f"Función: {pelicula_seleccionada.nombre}")
print(f"Asientos: {asientos_pedidos}")
print(f"Total Final: ${monto_final:.2f} (Ahorraste ${ahorro:.2f}) pesos")
print("Estado: PAGADA")