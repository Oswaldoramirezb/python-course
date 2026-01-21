"""
THREADING: QUEUE
================
Colas thread-safe
"""

print("=" * 50)
print("QUEUE - COLAS THREAD-SAFE")
print("=" * 50)

import threading
import queue
import time

# Crear cola
cola = queue.Queue()

print("\nQueue thread-safe:")
print("  import queue")
print("  cola = queue.Queue()")

# Productor
def productor():
    """Producir elementos"""
    for i in range(5):
        time.sleep(0.1)
        cola.put(f"Elemento {i}")
        print(f"  Productor: Agregó elemento {i}")

# Consumidor
def consumidor():
    """Consumir elementos"""
    while True:
        elemento = cola.get()
        if elemento is None:
            break
        print(f"  Consumidor: Procesó {elemento}")
        cola.task_done()

print("\nProductor-Consumidor:")
print("  productor() - Agrega elementos")
print("  consumidor() - Procesa elementos")

# Crear hilos
thread_prod = threading.Thread(target=productor)
thread_cons = threading.Thread(target=consumidor)

thread_prod.start()
thread_cons.start()

thread_prod.join()
cola.put(None)  # Señal de fin
thread_cons.join()

print("\nMétodos de Queue:")
print("  queue.put(item) - Agregar elemento")
print("  queue.get() - Obtener elemento")
print("  queue.task_done() - Marcar tarea completada")
print("  queue.join() - Esperar que todas las tareas terminen")

# Queue con límite
cola_limitada = queue.Queue(maxsize=3)
print("\nQueue con límite:")
print("  queue.Queue(maxsize=3)")

print("\nTipos de Queue:")
print("  Queue - FIFO (First In First Out)")
print("  LifoQueue - LIFO (Last In First Out)")
print("  PriorityQueue - Por prioridad")

print("\nVentajas:")
print("  ✅ Thread-safe")
print("  ✅ Sincronización automática")
print("  ✅ Útil para productor-consumidor")

print("\n" + "=" * 50)
