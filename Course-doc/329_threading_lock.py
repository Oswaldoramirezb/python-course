"""
THREADING: LOCK
===============
Sincronización con locks
"""

print("=" * 50)
print("LOCK - SINCRONIZACIÓN")
print("=" * 50)

import threading

# Recurso compartido
contador = 0
lock = threading.Lock()

def incrementar():
    """Incrementar contador de forma segura"""
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

print("\nLock básico:")
print("  lock = threading.Lock()")
print("  with lock:")
print("      # código crítico")

# Sin lock (puede haber problemas)
print("\nSin lock (problemas potenciales):")
print("  contador += 1  # No thread-safe")

# Con lock (seguro)
print("\nCon lock (thread-safe):")
print("  with lock:")
print("      contador += 1")

# Ejemplo práctico
def tarea_segura(nombre):
    """Tarea con lock"""
    global contador
    for _ in range(5):
        with lock:
            valor_actual = contador
            time.sleep(0.01)  # Simular procesamiento
            contador = valor_actual + 1
            print(f"  {nombre}: contador = {contador}")

import time
contador = 0
thread1 = threading.Thread(target=tarea_segura, args=("Hilo1",))
thread2 = threading.Thread(target=tarea_segura, args=("Hilo2",))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f"\nContador final: {contador}")

# RLock (reentrant lock)
print("\nRLock (reentrant):")
print("  rlock = threading.RLock()")
print("  - Permite adquirir el mismo lock múltiples veces")
print("  - Útil en funciones recursivas")

print("\nVentajas de lock:")
print("  ✅ Prevenir race conditions")
print("  ✅ Sincronizar acceso a recursos")
print("  ✅ Thread-safe")

print("\n" + "=" * 50)
