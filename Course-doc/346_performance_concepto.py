"""
PERFORMANCE: CONCEPTO
=====================
Optimización y rendimiento
"""

print("=" * 50)
print("CONCEPTO DE PERFORMANCE")
print("=" * 50)

import time

print("\nPerformance:")
print("  - Velocidad de ejecución")
print("  - Uso de memoria")
print("  - Eficiencia del código")

print("\nMétricas:")
print("  Tiempo de ejecución")
print("  Uso de memoria")
print("  Complejidad algorítmica")
print("  Throughput")

print("\nHerramientas:")
print("  timeit - Medir tiempo")
print("  cProfile - Profiling")
print("  memory_profiler - Memoria")
print("  line_profiler - Por línea")

print("\nTécnicas de optimización:")
print("  ✅ Elegir algoritmos eficientes")
print("  ✅ Usar estructuras de datos apropiadas")
print("  ✅ Evitar operaciones costosas")
print("  ✅ Cachear resultados")
print("  ✅ Usar generadores")
print("  ✅ Optimizar bucles")

print("\nPrincipio:")
print("  'Premature optimization is the root of all evil'")
print("  - Optimizar solo cuando sea necesario")
print("  - Medir primero, optimizar después")

print("\nEjemplo - Comparar tiempos:")
def funcion_lenta():
    suma = 0
    for i in range(1000000):
        suma += i
    return suma

inicio = time.time()
resultado = funcion_lenta()
tiempo = time.time() - inicio
print(f"\nTiempo de ejecución: {tiempo:.4f} segundos")

print("\n" + "=" * 50)
