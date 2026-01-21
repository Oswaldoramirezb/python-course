"""
RESUMEN: FUNCTOOLS
==================
Todas las funciones de functools
"""

print("=" * 50)
print("RESUMEN - FUNCTOOLS")
print("=" * 50)

print("\nImportar:")
print("  from functools import ...")

print("\nFunciones principales:")
print("  reduce(func, iterable, initial) - Reducir secuencia")
print("  partial(func, *args, **kwargs) - Función parcial")
print("  lru_cache(maxsize) - Cache de resultados")
print("  wraps(func) - Preservar metadatos")
print("  singledispatch - Dispatch por tipo")

print("\nReduce:")
print("  reduce(lambda x, y: x + y, [1,2,3]) → 6")
print("  Equivalente a sum([1,2,3])")

print("\nPartial:")
print("  multiplicar_2 = partial(multiplicar, 2)")
print("  multiplicar_2(3) → multiplicar(2, 3)")

print("\nLRU Cache:")
print("  @lru_cache(maxsize=128)")
print("  def funcion_costosa(n): ...")

print("\nVentajas:")
print("  ✅ Funciones más poderosas")
print("  ✅ Optimización")
print("  ✅ Reutilización de código")

print("\nUso:")
print("  - Reducir secuencias")
print("  - Crear funciones parciales")
print("  - Cachear resultados")
print("  - Preservar metadatos")

print("\n" + "=" * 50)
