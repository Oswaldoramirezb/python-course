"""
SET: DIFERENCIA
===============
Elementos que están en el primer set pero NO en el segundo
"""

print("=" * 50)
print("DIFERENCIA DE SETS")
print("=" * 50)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")

# Diferencia con -
diferencia = set1 - set2
print(f"\nDiferencia (set1 - set2): {diferencia}")
print(f"  (elementos en set1 pero no en set2)")

# Diferencia con método
diferencia2 = set1.difference(set2)
print(f"Diferencia con difference(): {diferencia2}")

# Diferencia inversa
diferencia3 = set2 - set1
print(f"\nDiferencia (set2 - set1): {diferencia3}")

print("\n" + "=" * 50)
