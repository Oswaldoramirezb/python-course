"""
SET: INTERSECCIÓN
=================
Elementos que están en AMBOS sets
"""

print("=" * 50)
print("INTERSECCIÓN DE SETS")
print("=" * 50)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")

# Intersección con &
interseccion = set1 & set2
print(f"\nIntersección con &: {interseccion}")

# Intersección con método
interseccion2 = set1.intersection(set2)
print(f"Intersección con intersection(): {interseccion2}")

# Solo elementos comunes
print(f"\nElementos comunes: {interseccion}")

print("\n" + "=" * 50)
