"""
LISTA: SLICING
===============
Extraer partes de una lista
"""

print("=" * 50)
print("LISTA SLICING")
print("=" * 50)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nLista: {lista}")

print(f"\nSlicing básico:")
print(f"  lista[2:5] = {lista[2:5]} (del índice 2 al 4)")
print(f"  lista[:3] = {lista[:3]} (desde inicio hasta 2)")
print(f"  lista[3:] = {lista[3:]} (desde índice 3 hasta final)")
print(f"  lista[:] = {lista[:]} (toda la lista)")

print(f"\nSlicing con paso:")
print(f"  lista[::2] = {lista[::2]} (cada 2 elementos)")
print(f"  lista[::-1] = {lista[::-1]} (lista invertida)")

print("\n" + "=" * 50)
