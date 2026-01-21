"""
TUPLA: ACCEDER A ELEMENTOS
==========================
Obtener elementos de una tupla
"""

print("=" * 50)
print("ACCEDER A ELEMENTOS DE TUPLA")
print("=" * 50)

tupla = (10, 20, 30, 40, 50)
print(f"\nTupla: {tupla}")

print(f"  tupla[0] = {tupla[0]} (primer elemento)")
print(f"  tupla[2] = {tupla[2]} (tercer elemento)")
print(f"  tupla[-1] = {tupla[-1]} (último elemento)")
print(f"  tupla[-2] = {tupla[-2]} (penúltimo elemento)")

# Slicing
print(f"\nSlicing (rebanadas):")
print(f"  tupla[1:4] = {tupla[1:4]} (del índice 1 al 3)")
print(f"  tupla[:3] = {tupla[:3]} (desde inicio hasta 2)")
print(f"  tupla[2:] = {tupla[2:]} (desde índice 2 hasta final)")

print("\n" + "=" * 50)
