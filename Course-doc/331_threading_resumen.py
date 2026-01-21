"""
RESUMEN: THREADING
==================
Todas las operaciones con threading
"""

print("=" * 50)
print("RESUMEN - THREADING")
print("=" * 50)

print("\nConcepto:")
print("  - Ejecutar código en paralelo")
print("  - Múltiples hilos en un proceso")
print("  - Compartir memoria")

print("\nCrear hilo:")
print("  import threading")
print("  thread = threading.Thread(target=funcion, args=(arg1,))")
print("  thread.start()")
print("  thread.join()")

print("\nCon clase:")
print("  class MiHilo(threading.Thread):")
print("      def run(self):")
print("          # código")

print("\nSincronización:")
print("  lock = threading.Lock()")
print("  with lock:")
print("      # código crítico")
print("")
print("  rlock = threading.RLock()  # Reentrant")

print("\nQueue:")
print("  import queue")
print("  cola = queue.Queue()")
print("  cola.put(item)")
print("  item = cola.get()")

print("\nVentajas:")
print("  ✅ Ejecución paralela")
print("  ✅ Mejor uso de CPU")
print("  ✅ Responsividad en I/O")

print("\nLimitaciones:")
print("  ⚠️  GIL limita paralelismo real")
print("  ⚠️  Mejor para I/O que CPU")
print("  ⚠️  Para CPU usar multiprocessing")

print("\nCuándo usar:")
print("  - Operaciones I/O")
print("  - Tareas independientes")
print("  - Interfaces responsivas")

print("\nBibliotecas:")
print("  threading - Incluido en Python")
print("  concurrent.futures - Más simple")

print("\n" + "=" * 50)
