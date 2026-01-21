"""
SET: AGREGAR Y ELIMINAR
=======================
Agregar y eliminar elementos de sets
"""

print("=" * 50)
print("AGREGAR Y ELIMINAR EN SETS")
print("=" * 50)

mi_set = {1, 2, 3}
print(f"\nSet original: {mi_set}")

# add() - agregar un elemento
mi_set.add(4)
print(f"Después de add(4): {mi_set}")

# update() - agregar múltiples elementos
mi_set.update([5, 6])
print(f"Después de update([5, 6]): {mi_set}")

# remove() - eliminar (error si no existe)
mi_set.remove(1)
print(f"Después de remove(1): {mi_set}")

# discard() - eliminar (no da error si no existe)
mi_set.discard(10)  # No existe, pero no da error
print(f"Después de discard(10): {mi_set}")

# pop() - eliminar y retornar elemento aleatorio
elemento = mi_set.pop()
print(f"Después de pop(): {mi_set}, elemento eliminado: {elemento}")

print("\n" + "=" * 50)
