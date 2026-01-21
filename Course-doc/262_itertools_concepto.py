"""
ITERTOOLS: CONCEPTO
===================
Herramientas para trabajar con iteradores
"""

print("=" * 50)
print("CONCEPTO DE ITERTOOLS")
print("=" * 50)

from itertools import count, cycle, repeat

print("\nitertools:")
print("  - Módulo con herramientas para iteradores")
print("  - Funciones eficientes y optimizadas")
print("  - Útil para combinaciones, permutaciones, etc.")

print("\nFunciones principales:")
print("  count() - Contador infinito")
print("  cycle() - Ciclo infinito")
print("  repeat() - Repetir valor")
print("  combinations() - Combinaciones")
print("  permutations() - Permutaciones")
print("  product() - Producto cartesiano")

print("\nEjemplo - count:")
contador = count(start=1, step=2)
print("  contador = count(start=1, step=2)")
print("  Primeros 5 valores:", [next(contador) for _ in range(5)])

print("\nVentajas:")
print("  ✅ Eficiencia de memoria")
print("  ✅ Iteradores lazy")
print("  ✅ Funciones optimizadas")

print("\nUso:")
print("  - Generar secuencias")
print("  - Combinaciones y permutaciones")
print("  - Agrupar y filtrar")

print("\n" + "=" * 50)
