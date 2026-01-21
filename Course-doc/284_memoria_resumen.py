"""
RESUMEN: MEMORIA Y GARBAGE COLLECTION
======================================
Todas las operaciones con memoria
"""

print("=" * 50)
print("RESUMEN - MEMORIA Y GC")
print("=" * 50)

print("\nGestión de memoria:")
print("  - Python maneja automáticamente")
print("  - Garbage Collector libera memoria")
print("  - Contador de referencias")

print("\nReferencias:")
print("  a = [1, 2, 3]")
print("  b = a  # Misma referencia")
print("  id(a) == id(b) → True")
print("  a is b → True")

print("\nGarbage Collection:")
print("  - Libera objetos sin referencias")
print("  - Automático")
print("  - gc.collect() para forzar")
print("  - Detecta ciclos de referencias")

print("\nReferencias débiles:")
print("  import weakref")
print("  ref = weakref.ref(objeto)")
print("  - No evita eliminación")
print("  - Útil para caches y callbacks")

print("\nOptimización:")
print("  ✅ Usar generadores")
print("  ✅ __slots__ en clases")
print("  ✅ Eliminar referencias innecesarias")
print("  ✅ Reutilizar objetos")

print("\nMódulos:")
print("  sys.getsizeof() - Tamaño de objeto")
print("  sys.getrefcount() - Contador de referencias")
print("  gc - Garbage Collection")
print("  weakref - Referencias débiles")

print("\n" + "=" * 50)
