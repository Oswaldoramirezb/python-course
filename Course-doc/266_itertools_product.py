"""
ITERTOOLS: PRODUCT
=================
Producto cartesiano
"""

print("=" * 50)
print("PRODUCT - PRODUCTO CARTESIANO")
print("=" * 50)

from itertools import product

# product() - Producto cartesiano
lista1 = [1, 2]
lista2 = ["A", "B"]

producto = list(product(lista1, lista2))
print(f"\nProducto cartesiano:")
print(f"  lista1 = {lista1}")
print(f"  lista2 = {lista2}")
print(f"  product(lista1, lista2) = {producto}")

# Múltiples iterables
lista3 = ["X", "Y"]
producto_multi = list(product(lista1, lista2, lista3))
print(f"\nProducto de 3 listas (total: {len(producto_multi)}):")
for p in producto_multi:
    print(f"  {p}")

# Con repetición
producto_rep = list(product([0, 1], repeat=3))
print(f"\nProducto con repetición (repeat=3):")
print(f"  {producto_rep}")

# Ejemplo práctico - Generar contraseñas
caracteres = ["a", "b", "c"]
longitud = 2
contraseñas = [''.join(p) for p in product(caracteres, repeat=longitud)]
print(f"\nContraseñas de longitud {longitud}:")
print(f"  {contraseñas}")

print("\n" + "=" * 50)
