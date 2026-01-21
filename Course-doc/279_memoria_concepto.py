"""
MEMORIA: CONCEPTO
=================
Gestión de memoria en Python
"""

print("=" * 50)
print("CONCEPTO DE MEMORIA")
print("=" * 50)

import sys

print("\nGestión de memoria:")
print("  - Python maneja memoria automáticamente")
print("  - Garbage Collector libera memoria")
print("  - Referencias cuentan objetos")

print("\nConceptos:")
print("  Referencia - Apuntador a objeto")
print("  Contador de referencias - Cuántas referencias")
print("  Garbage Collection - Liberar memoria no usada")

# Ver tamaño de objetos
numero = 42
texto = "Python"
lista = [1, 2, 3]

print("\nTamaño de objetos:")
print(f"  sys.getsizeof({numero}) = {sys.getsizeof(numero)} bytes")
print(f"  sys.getsizeof('{texto}') = {sys.getsizeof(texto)} bytes")
print(f"  sys.getsizeof({lista}) = {sys.getsizeof(lista)} bytes")

print("\nReferencias:")
print("  a = [1, 2, 3]")
print("  b = a  # b referencia al mismo objeto")
print("  id(a) == id(b) → True")

print("\nGarbage Collection:")
print("  - Libera objetos sin referencias")
print("  - Automático en Python")
print("  - Puede ser manual con gc.collect()")

print("\n" + "=" * 50)
