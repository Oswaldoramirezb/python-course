"""
SET: UNIÓN
==========
Combinar dos sets (todos los elementos únicos)
"""

print("=" * 50)
print("UNIÓN DE SETS")
print("=" * 50)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")

# Unión con |
union = set1 | set2
print(f"\nUnión con |: {union}")

# Unión con método
union2 = set1.union(set2)
print(f"Unión con union(): {union2}")

# Unión con múltiples sets
set3 = {7, 8}
union3 = set1 | set2 | set3
print(f"\nUnión de 3 sets: {union3}")

print("\n" + "=" * 50)
