"""
PERFORMANCE: PROFILING
======================
Analizar rendimiento del código
"""

print("=" * 50)
print("PROFILING - ANÁLISIS DE RENDIMIENTO")
print("=" * 50)

import cProfile
import pstats

# Función a analizar
def funcion_compleja():
    """Función con múltiples operaciones"""
    resultado = []
    for i in range(1000):
        resultado.append(i * 2)
    
    suma = 0
    for elemento in resultado:
        suma += elemento
    
    return suma

print("\nProfiling con cProfile:")
print("  import cProfile")
print("  profiler = cProfile.Profile()")
print("  profiler.enable()")
print("  # código")
print("  profiler.disable()")
print("  profiler.print_stats()")

# Crear profiler
profiler = cProfile.Profile()
profiler.enable()

# Ejecutar código
for _ in range(100):
    funcion_compleja()

profiler.disable()

print("\nEstadísticas:")
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10

print("\nInformación del profiling:")
print("  ncalls - Número de llamadas")
print("  tottime - Tiempo total (sin subfunciones)")
print("  cumtime - Tiempo acumulado (con subfunciones)")
print("  percall - Tiempo por llamada")

print("\nGuardar resultados:")
print("  profiler.dump_stats('perfil.prof')")
print("  # Ver con: python -m pstats perfil.prof")

print("\nVentajas:")
print("  ✅ Identificar cuellos de botella")
print("  ✅ Ver dónde se gasta el tiempo")
print("  ✅ Optimizar las partes correctas")

print("\nHerramientas:")
print("  cProfile - Incluido en Python")
print("  line_profiler - Por línea")
print("  memory_profiler - Uso de memoria")

print("\n" + "=" * 50)
