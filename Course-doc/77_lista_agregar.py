"""
LISTA: AGREGAR ELEMENTOS
========================
Agregar elementos a una lista
"""

print("=" * 50)
print("AGREGAR ELEMENTOS A LISTA")
print("=" * 50)

lista = [1, 2, 3]
print(f"\nLista original: {lista}")

# append() - agregar al final
lista.append(4)
print(f"Después de append(4): {lista}")

# insert() - insertar en posición específica
lista.insert(1, 10)
print(f"Después de insert(1, 10): {lista}")

# extend() - agregar múltiples elementos
lista.extend([5, 6])
print(f"Después de extend([5, 6]): {lista}")

# Con operador +
lista2 = lista + [7, 8]
print(f"Con +: {lista} + [7, 8] = {lista2}")

print("\n" + "=" * 50)
