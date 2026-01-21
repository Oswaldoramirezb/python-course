"""
ITERTOOLS: COMBINATIONS
=======================
Generar combinaciones
"""

print("=" * 50)
print("COMBINATIONS")
print("=" * 50)

from itertools import combinations

# combinations() - Combinaciones sin repetición
elementos = ["A", "B", "C", "D"]

print(f"\nElementos: {elementos}")

# Combinaciones de 2
combinaciones_2 = list(combinations(elementos, 2))
print("\nCombinaciones de 2:")
for combo in combinaciones_2:
    print(f"  {combo}")

# Combinaciones de 3
combinaciones_3 = list(combinations(elementos, 3))
print(f"\nCombinaciones de 3 (total: {len(combinaciones_3)}):")
for combo in combinaciones_3:
    print(f"  {combo}")

# combinations_with_replacement - Con repetición
from itertools import combinations_with_replacement
combinaciones_rep = list(combinations_with_replacement(elementos[:3], 2))
print("\nCombinaciones con repetición de ['A', 'B', 'C']:")
for combo in combinaciones_rep:
    print(f"  {combo}")

print("\nUso:")
print("  ✅ Combinaciones de elementos")
print("  ✅ Análisis combinatorio")
print("  ✅ Generar subconjuntos")

print("\n" + "=" * 50)
