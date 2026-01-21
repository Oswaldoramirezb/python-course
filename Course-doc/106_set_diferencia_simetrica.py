"""
SET: DIFERENCIA SIMÉTRICA
=========================
Elementos que están en UNO u OTRO set, pero NO en ambos
"""

print("=" * 50)
print("DIFERENCIA SIMÉTRICA DE SETS")
print("=" * 50)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")

# Diferencia simétrica con ^
diferencia_simetrica = set1 ^ set2
print(f"\nDiferencia simétrica con ^: {diferencia_simetrica}")
print(f"  (elementos en uno u otro, pero no en ambos)")

# Diferencia simétrica con método
diferencia_simetrica2 = set1.symmetric_difference(set2)
print(f"Diferencia simétrica con symmetric_difference(): {diferencia_simetrica2}")

print("\n" + "=" * 50)
