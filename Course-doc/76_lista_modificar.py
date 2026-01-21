"""
LISTA: MODIFICAR ELEMENTOS
==========================
Cambiar valores en una lista
"""

print("=" * 50)
print("MODIFICAR ELEMENTOS DE LISTA")
print("=" * 50)

lista = [1, 2, 3, 4, 5]
print(f"\nLista original: {lista}")

# Modificar un elemento
lista[0] = 10
print(f"Después de lista[0] = 10: {lista}")

# Modificar múltiples elementos
lista[1:3] = [20, 30]
print(f"Después de lista[1:3] = [20, 30]: {lista}")

# Agregar al final
lista.append(6)
print(f"Después de append(6): {lista}")

print("\n" + "=" * 50)
