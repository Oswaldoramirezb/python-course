"""
FUNCTOOLS: CONCEPTO
===================
Herramientas para funciones de orden superior
"""

print("=" * 50)
print("CONCEPTO DE FUNCTOOLS")
print("=" * 50)

from functools import reduce, partial, lru_cache

print("\nfunctools:")
print("  - Módulo con herramientas para funciones")
print("  - Funciones de orden superior")
print("  - Optimización y decoradores")

print("\nFunciones principales:")
print("  reduce() - Reducir secuencia a un valor")
print("  partial() - Función parcial")
print("  lru_cache() - Cache de resultados")
print("  wraps() - Preservar metadatos")
print("  singledispatch() - Dispatch por tipo")

print("\nEjemplo - reduce:")
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(f"  reduce(lambda x, y: x + y, {numeros}) = {suma}")

print("\nVentajas:")
print("  ✅ Funciones más poderosas")
print("  ✅ Optimización")
print("  ✅ Reutilización de código")

print("\nUso:")
print("  - Reducir secuencias")
print("  - Crear funciones parciales")
print("  - Cachear resultados")

print("\n" + "=" * 50)
