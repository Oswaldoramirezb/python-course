"""
THREADING: CONCEPTO
==================
Programación con hilos
"""

print("=" * 50)
print("CONCEPTO DE THREADING")
print("=" * 50)

import threading

print("\nThreading:")
print("  - Ejecutar código en paralelo")
print("  - Múltiples hilos en un proceso")
print("  - Compartir memoria")

print("\nConceptos:")
print("  Thread - Hilo de ejecución")
print("  GIL - Global Interpreter Lock")
print("  Lock - Sincronización")
print("  Queue - Cola thread-safe")

print("\nVentajas:")
print("  ✅ Ejecución paralela")
print("  ✅ Mejor uso de CPU")
print("  ✅ Responsividad en I/O")

print("\nLimitaciones (GIL):")
print("  ⚠️  GIL limita paralelismo real en CPU")
print("  ⚠️  Mejor para I/O que para CPU")
print("  ⚠️  Para CPU intensivo usar multiprocessing")

print("\nCuándo usar:")
print("  - Operaciones I/O (red, archivos)")
print("  - Tareas independientes")
print("  - Interfaces responsivas")

print("\nBiblioteca:")
print("  threading - Incluido en Python")
print("  concurrent.futures - Más simple")

print("\nEjemplo básico:")
print("  import threading")
print("  thread = threading.Thread(target=funcion)")
print("  thread.start()")
print("  thread.join()")

print("\n" + "=" * 50)
