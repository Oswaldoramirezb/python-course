"""
LISTA: ACCEDER A ELEMENTOS
==========================
Obtener elementos de una lista
"""

print("=" * 50)
print("ACCEDER A ELEMENTOS DE LISTA")
print("=" * 50)

lista = [10, 20, 30, 40, 50]
print(f"\nLista: {lista}")

print(f"  lista[0] = {lista[0]} (primer elemento)")
print(f"  lista[2] = {lista[2]} (tercer elemento)")
print(f"  lista[-1] = {lista[-1]} (último elemento)")
print(f"  lista[-2] = {lista[-2]} (penúltimo elemento)")

# Slicing
print(f"\nSlicing (rebanadas):")
print(f"  lista[1:4] = {lista[1:4]} (del índice 1 al 3)")
print(f"  lista[:3] = {lista[:3]} (desde inicio hasta 2)")
print(f"  lista[2:] = {lista[2:]} (desde índice 2 hasta final)")

print("\n" + "=" * 50)
