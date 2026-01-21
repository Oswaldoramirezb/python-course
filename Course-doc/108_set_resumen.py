"""
RESUMEN: SETS
=============
Todas las operaciones importantes con sets
"""

print("=" * 50)
print("RESUMEN - SETS")
print("=" * 50)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")

print(f"\nCaracterísticas:")
print(f"  ✅ No permiten duplicados")
print(f"  ✅ No tienen orden")
print(f"  ✅ Elementos deben ser hashables")

print(f"\nOperaciones:")
print(f"  Crear: mi_set = {{1, 2, 3}}")
print(f"  Agregar: mi_set.add(4)")
print(f"  Eliminar: mi_set.remove(1)")
print(f"  Unión: set1 | set2 = {set1 | set2}")
print(f"  Intersección: set1 & set2 = {set1 & set2}")
print(f"  Diferencia: set1 - set2 = {set1 - set2}")
print(f"  Diferencia simétrica: set1 ^ set2 = {set1 ^ set2}")

print("\n" + "=" * 50)
