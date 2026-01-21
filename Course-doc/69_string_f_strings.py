"""
STRING: F-STRINGS
==================
Formateo moderno de cadenas (Python 3.6+)
"""

print("=" * 50)
print("F-STRINGS")
print("=" * 50)

# f-strings básico
nombre = "Juan"
edad = 25
print(f"\nEjemplo básico:")
print(f"  nombre = '{nombre}', edad = {edad}")
mensaje = f"Mi nombre es {nombre} y tengo {edad} años"
print(f"  f'Mi nombre es {{nombre}} y tengo {{edad}} años'")
print(f"  Resultado: '{mensaje}'")

# f-strings con expresiones
a = 10
b = 5
print(f"\nCon expresiones:")
print(f"  a = {a}, b = {b}")
resultado = f"La suma es {a + b}"
print(f"  f'La suma es {{a + b}}' = '{resultado}'")

# f-strings con formateo
precio = 19.99
print(f"\nCon formateo:")
print(f"  precio = {precio}")
print(f"  f'Precio: ${{precio:.2f}}' = 'Precio: ${precio:.2f}'")

print("\n" + "=" * 50)
