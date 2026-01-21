"""
THREADING: THREAD
=================
Crear y ejecutar hilos
"""

print("=" * 50)
print("THREAD - CREAR HILOS")
print("=" * 50)

import threading
import time

# Función a ejecutar en hilo
def tarea(nombre, tiempo):
    """Tarea que se ejecuta en hilo"""
    print(f"  Hilo {nombre}: Iniciando...")
    time.sleep(tiempo)
    print(f"  Hilo {nombre}: Completado")

print("\nCrear y ejecutar hilo:")
print("  thread = threading.Thread(target=tarea, args=('Hilo1', 1))")
print("  thread.start()")
print("  thread.join()")

# Crear hilo
thread1 = threading.Thread(target=tarea, args=("Hilo1", 0.5))
thread2 = threading.Thread(target=tarea, args=("Hilo2", 0.5))

print("\nEjecutar hilos:")
thread1.start()
thread2.start()

# Esperar que terminen
thread1.join()
thread2.join()

print("\nHilos completados")

# Hilo con clase
class MiHilo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    
    def run(self):
        print(f"  Hilo {self.nombre}: Ejecutando...")
        time.sleep(0.3)
        print(f"  Hilo {self.nombre}: Completado")

print("\nHilo con clase:")
print("  class MiHilo(threading.Thread):")
print("      def run(self):")
print("          # código")

hilo3 = MiHilo("Hilo3")
hilo3.start()
hilo3.join()

print("\nMétodos:")
print("  thread.start() - Iniciar hilo")
print("  thread.join() - Esperar que termine")
print("  thread.is_alive() - Verificar si está vivo")

print("\n" + "=" * 50)
