"""
LISTA: ORDENAR
==============
Ordenar elementos de una lista
"""

print("=" * 50)
print("ORDENAR LISTAS")
print("=" * 50)

lista = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nLista original: {lista}")

# sort() - ordena in-place
lista.sort()
print(f"Después de sort(): {lista}")

# sort() descendente
lista2 = [3, 1, 4, 1, 5]
lista2.sort(reverse=True)
print(f"\nsort(reverse=True): {lista2}")

# sorted() - retorna nueva lista ordenada
lista3 = [3, 1, 4, 1, 5]
lista_ordenada = sorted(lista3)
print(f"\n  Original: {lista3}")
print(f"  Ordenada: {lista_ordenada}")

# Ordenar cadenas
palabras = ["banana", "apple", "cherry"]
palabras.sort()
print(f"\nOrdenar cadenas: {palabras}")

print("\n" + "=" * 50)
