"""
LISTA: ELIMINAR ELEMENTOS
==========================
Eliminar elementos de una lista
"""

print("=" * 50)
print("ELIMINAR ELEMENTOS DE LISTA")
print("=" * 50)

lista = [1, 2, 3, 4, 5, 3]
print(f"\nLista original: {lista}")

# remove() - eliminar por valor
lista.remove(3)
print(f"Después de remove(3): {lista}")

# pop() - eliminar por índice (retorna el valor)
elemento = lista.pop()
print(f"Después de pop(): {lista}, elemento eliminado: {elemento}")

# del - eliminar por índice
del lista[0]
print(f"Después de del lista[0]: {lista}")

# clear() - vaciar lista
lista.clear()
print(f"Después de clear(): {lista}")

print("\n" + "=" * 50)
