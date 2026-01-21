"""
ITERTOOLS: COUNT Y CYCLE
========================
Generadores infinitos
"""

print("=" * 50)
print("COUNT Y CYCLE")
print("=" * 50)

from itertools import count, cycle

# count() - Contador infinito
print("\ncount() - Contador infinito:")
contador = count(start=0, step=1)
print("  contador = count(start=0, step=1)")
print("  Primeros 5:", [next(contador) for _ in range(5)])

contador2 = count(start=10, step=-2)
print("\n  contador2 = count(start=10, step=-2)")
print("  Primeros 5:", [next(contador2) for _ in range(5)])

# cycle() - Ciclo infinito
print("\ncycle() - Ciclo infinito:")
ciclo = cycle(["A", "B", "C"])
print("  ciclo = cycle(['A', 'B', 'C'])")
print("  Primeros 7:", [next(ciclo) for _ in range(7)])

# repeat() - Repetir valor
from itertools import repeat
print("\nrepeat() - Repetir valor:")
repetidor = repeat("Hola", times=3)
print("  repetidor = repeat('Hola', times=3)")
print(f"  Valores: {list(repetidor)}")

print("\nUso:")
print("  ✅ Generar índices")
print("  ✅ Alternar valores")
print("  ✅ Repetir valores")

print("\n" + "=" * 50)
