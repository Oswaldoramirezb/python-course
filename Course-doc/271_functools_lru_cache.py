"""
FUNCTOOLS: LRU_CACHE
====================
Cache de resultados (memoización)
"""

print("=" * 50)
print("LRU_CACHE - MEMOIZACIÓN")
print("=" * 50)

from functools import lru_cache

# Sin cache
def fibonacci_sin_cache(n):
    if n <= 1:
        return n
    return fibonacci_sin_cache(n-1) + fibonacci_sin_cache(n-2)

# Con cache
@lru_cache(maxsize=128)
def fibonacci_con_cache(n):
    if n <= 1:
        return n
    return fibonacci_con_cache(n-1) + fibonacci_con_cache(n-2)

print("\nComparación:")
print("  Sin cache: fibonacci_sin_cache(30) - Lento")
print("  Con cache: fibonacci_con_cache(30) - Rápido")

import time

# Medir tiempo con cache
inicio = time.time()
resultado = fibonacci_con_cache(30)
tiempo = time.time() - inicio
print(f"\nCon @lru_cache:")
print(f"  fibonacci_con_cache(30) = {resultado}")
print(f"  Tiempo: {tiempo:.4f} segundos")

# Segunda llamada (más rápida, usa cache)
inicio2 = time.time()
resultado2 = fibonacci_con_cache(30)
tiempo2 = time.time() - inicio2
print(f"\nSegunda llamada (desde cache):")
print(f"  Tiempo: {tiempo2:.4f} segundos")

# Información del cache
print(f"\nInformación del cache:")
print(f"  fibonacci_con_cache.cache_info() = {fibonacci_con_cache.cache_info()}")

print("\nVentajas:")
print("  ✅ Acelera funciones costosas")
print("  ✅ Evita cálculos repetidos")
print("  ✅ Fácil de usar")

print("\n" + "=" * 50)
