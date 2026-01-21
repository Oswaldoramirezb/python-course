"""
GARBAGE COLLECTION
==================
Recolección automática de basura
"""

print("=" * 50)
print("GARBAGE COLLECTION")
print("=" * 50)

import gc

print("\nGarbage Collection:")
print("  - Libera objetos sin referencias")
print("  - Automático en Python")
print("  - Módulo gc para control manual")

# Contador de referencias
import sys

objeto = [1, 2, 3]
print(f"\nContador de referencias:")
print(f"  sys.getrefcount(objeto) = {sys.getrefcount(objeto)}")

# Crear más referencias
ref1 = objeto
ref2 = objeto
print(f"\nCrear más referencias:")
print(f"  ref1 = objeto")
print(f"  ref2 = objeto")
print(f"  sys.getrefcount(objeto) = {sys.getrefcount(objeto)}")

# Eliminar referencias
del ref1, ref2
print(f"\nEliminar referencias:")
print(f"  del ref1, ref2")
print(f"  sys.getrefcount(objeto) = {sys.getrefcount(objeto)}")

# Garbage Collection manual
print("\nGarbage Collection manual:")
print("  gc.collect() - Forzar recolección")
print("  gc.get_count() - Ver contadores")
print("  gc.get_stats() - Ver estadísticas")

contadores = gc.get_count()
print(f"  gc.get_count() = {contadores}")

print("\nCiclos de referencias:")
print("  - Objetos que se referencian entre sí")
print("  - GC los detecta y libera")
print("  - Útil para objetos complejos")

print("\n" + "=" * 50)
