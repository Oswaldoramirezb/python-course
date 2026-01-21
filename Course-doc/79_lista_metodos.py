"""
LISTA: MÉTODOS ÚTILES
======================
Métodos importantes de las listas
"""

print("=" * 50)
print("MÉTODOS DE LISTAS")
print("=" * 50)

lista = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nLista: {lista}")

print(f"\nMétodos útiles:")
print(f"  len(lista) = {len(lista)}")
print(f"  max(lista) = {max(lista)}")
print(f"  min(lista) = {min(lista)}")
print(f"  sum(lista) = {sum(lista)}")
print(f"  lista.count(1) = {lista.count(1)}")
print(f"  lista.index(4) = {lista.index(4)}")

# Ordenar
lista2 = [3, 1, 4, 1, 5]
lista2.sort()
print(f"\n  lista.sort() → {lista2}")

# Revertir
lista3 = [1, 2, 3]
lista3.reverse()
print(f"  lista.reverse() → {lista3}")

print("\n" + "=" * 50)
