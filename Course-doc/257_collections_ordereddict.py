"""
COLLECTIONS: ORDEREDDICT
========================
Diccionario que mantiene orden de inserción
"""

print("=" * 50)
print("ORDEREDDICT")
print("=" * 50)

from collections import OrderedDict

# OrderedDict mantiene orden
diccionario_ordenado = OrderedDict()
diccionario_ordenado["primero"] = 1
diccionario_ordenado["segundo"] = 2
diccionario_ordenado["tercero"] = 3

print("\nOrderedDict mantiene orden:")
print(f"  {dict(diccionario_ordenado)}")

# Mover al final
diccionario_ordenado.move_to_end("primero")
print(f"\nmove_to_end('primero'):")
print(f"  {dict(diccionario_ordenado)}")

# Comparación
print("\nComparación:")
print("  dict (Python 3.7+): También mantiene orden")
print("  OrderedDict: Garantiza orden en todas las versiones")

# Útil para LRU cache
print("\nÚtil para:")
print("  ✅ Mantener orden de inserción")
print("  ✅ Implementar LRU cache")
print("  ✅ Compatibilidad con Python < 3.7")

print("\n" + "=" * 50)
