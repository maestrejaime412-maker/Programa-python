# Problema 2: Gestión de precios de un menú de restaurante

# Matriz del menú: [Nombre del Producto, Categoría, Precio Base]
menu = [
    ["Hamburguesa BBQ", "Comida Rápida", 25000],
    ["Pizza Hawaiana", "Comida Rápida", 32000],
    ["Ensalada César", "Saludable", 18000],
    ["Salmón a la Plancha", "Mariscos", 45000],
    ["Jugo Natural", "Bebidas", 9000],
    ["Pasta Alfredo", "Italiana", 28000]
]

# Función para calcular el precio final
def calcular_precio_final(categoria, precio_base):
    categoria_objetivo = "Comida Rápida"
    umbral_precio = 20000

    # Aplicar descuento del 15%
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final

# Mostrar resultados
print("=== MENÚ DEL RESTAURANTE ===\n")

for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio Base: ${precio_base:,.0f}")
    print(f"Precio Final: ${precio_final:,.0f}")
    print("-" * 40)