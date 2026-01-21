"""
DICCIONARIO: KEYS, VALUES, ITEMS
=================================
Obtener claves, valores y pares
"""

print("=" * 50)
print("KEYS, VALUES, ITEMS")
print("=" * 50)

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(f"\nDiccionario: {persona}")

# keys() - solo claves
claves = persona.keys()
print(f"\nkeys(): {list(claves)}")

# values() - solo valores
valores = persona.values()
print(f"values(): {list(valores)}")

# items() - pares clave-valor
items = persona.items()
print(f"items(): {list(items)}")

# Iterar con cada uno
print(f"\nIterar con keys():")
for clave in persona.keys():
    print(f"  Clave: {clave}")

print(f"\nIterar con values():")
for valor in persona.values():
    print(f"  Valor: {valor}")

print(f"\nIterar con items():")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

print("\n" + "=" * 50)
