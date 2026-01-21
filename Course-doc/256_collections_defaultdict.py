"""
COLLECTIONS: DEFAULTDICT
========================
Diccionario con valor por defecto automático
"""

print("=" * 50)
print("DEFAULTDICT")
print("=" * 50)

from collections import defaultdict

# defaultdict con list
grupos = defaultdict(list)
grupos["frutas"].append("manzana")
grupos["frutas"].append("banana")
grupos["verduras"].append("zanahoria")

print("\ndefaultdict(list):")
print(f"  grupos = {dict(grupos)}")
print(f"  grupos['frutas'] = {grupos['frutas']}")
print(f"  grupos['nuevo'] = {grupos['nuevo']} (lista vacía automática)")

# defaultdict con int (contador)
contador = defaultdict(int)
palabras = ["a", "b", "a", "c", "b", "a"]

for palabra in palabras:
    contador[palabra] += 1

print(f"\ndefaultdict(int) - contador:")
print(f"  palabras = {palabras}")
print(f"  contador = {dict(contador)}")

# Comparación con dict normal
print("\nComparación:")
print("  dict normal: dict['nuevo'] → KeyError")
print("  defaultdict: dict['nuevo'] → valor por defecto")

print("\n" + "=" * 50)
