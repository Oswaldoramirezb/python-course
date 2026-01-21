"""
ITERTOOLS: PERMUTATIONS
=======================
Generar permutaciones
"""

print("=" * 50)
print("PERMUTATIONS")
print("=" * 50)

from itertools import permutations

# permutations() - Permutaciones
elementos = ["A", "B", "C"]

print(f"\nElementos: {elementos}")

# Todas las permutaciones
permutaciones = list(permutations(elementos))
print("\nTodas las permutaciones:")
for perm in permutaciones:
    print(f"  {perm}")

# Permutaciones de longitud específica
permutaciones_2 = list(permutations(elementos, 2))
print(f"\nPermutaciones de longitud 2 (total: {len(permutaciones_2)}):")
for perm in permutaciones_2:
    print(f"  {perm}")

# Ejemplo práctico - Anagramas
palabra = "ABC"
anagramas = [''.join(p) for p in permutations(palabra)]
print(f"\nAnagramas de '{palabra}':")
for anagrama in anagramas:
    print(f"  {anagrama}")

print("\nDiferencia con combinations:")
print("  combinations - Orden no importa: (A,B) = (B,A)")
print("  permutations - Orden importa: (A,B) ≠ (B,A)")

print("\n" + "=" * 50)
