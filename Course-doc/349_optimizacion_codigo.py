"""
PERFORMANCE: OPTIMIZACIÓN
========================
Técnicas de optimización
"""

print("=" * 50)
print("OPTIMIZACIÓN DE CÓDIGO")
print("=" * 50)

import timeit

print("\nTécnicas de optimización:")

# 1. Usar built-ins
print("\n1. Usar built-ins:")
codigo_lento = "suma = 0; [suma := suma + x for x in range(1000)]"
codigo_rapido = "sum(range(1000))"

tiempo_lento = timeit.timeit(codigo_lento, number=10000)
tiempo_rapido = timeit.timeit(codigo_rapido, number=10000)
print(f"  Lento: {tiempo_lento:.6f}s")
print(f"  Rápido: {tiempo_rapido:.6f}s")
print(f"  Mejora: {tiempo_lento/tiempo_rapido:.2f}x más rápido")

# 2. List comprehension vs bucle
print("\n2. List comprehension:")
bucle = "resultado = []; [resultado.append(x*2) for x in range(1000)]"
comp = "[x*2 for x in range(1000)]"

tiempo_bucle = timeit.timeit(bucle, number=10000)
tiempo_comp = timeit.timeit(comp, number=10000)
print(f"  Bucle: {tiempo_bucle:.6f}s")
print(f"  Comprehension: {tiempo_comp:.6f}s")

# 3. Cachear resultados
print("\n3. Cachear resultados:")
print("  from functools import lru_cache")
print("  @lru_cache(maxsize=128)")
print("  def funcion_costosa(n): ...")

# 4. Generadores
print("\n4. Usar generadores:")
print("  # Lista: [x**2 for x in range(1000000)]  # Todo en memoria")
print("  # Generador: (x**2 for x in range(1000000))  # Uno a uno")

# 5. Evitar operaciones costosas en bucles
print("\n5. Evitar operaciones costosas en bucles:")
print("  # Malo: for i in range(len(lista)):")
print("  # Bueno: for elemento in lista:")

print("\nReglas generales:")
print("  ✅ Medir antes de optimizar")
print("  ✅ Optimizar cuellos de botella")
print("  ✅ Usar algoritmos eficientes")
print("  ✅ Elegir estructuras de datos apropiadas")
print("  ✅ Evitar optimización prematura")

print("\nPrincipio 80/20:")
print("  - 80% del tiempo se gasta en 20% del código")
print("  - Optimizar solo ese 20%")

print("\n" + "=" * 50)
