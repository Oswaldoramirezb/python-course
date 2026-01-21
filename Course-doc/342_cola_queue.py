"""
ESTRUCTURAS: COLA (QUEUE)
=========================
FIFO - First In First Out
"""

print("=" * 50)
print("COLA (QUEUE) - FIFO")
print("=" * 50)

from collections import deque

# Implementar cola con deque
class Cola:
    """Cola implementada con deque"""
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Agregar elemento al final"""
        self.items.append(item)
    
    def dequeue(self):
        """Eliminar y retornar primer elemento"""
        if self.is_empty():
            raise IndexError("Cola vacía")
        return self.items.popleft()
    
    def front(self):
        """Ver primer elemento sin eliminarlo"""
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        """Verificar si está vacía"""
        return len(self.items) == 0
    
    def size(self):
        """Tamaño de la cola"""
        return len(self.items)

print("\nImplementar cola:")
print("  class Cola:")
print("      def enqueue(self, item): ...")
print("      def dequeue(self): ...")
print("      def front(self): ...")

# Usar cola
cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print(f"\nOperaciones:")
print(f"  enqueue(1), enqueue(2), enqueue(3)")
print(f"  front() = {cola.front()}")
print(f"  dequeue() = {cola.dequeue()}")
print(f"  dequeue() = {cola.dequeue()}")
print(f"  size() = {cola.size()}")

print("\nCaracterísticas:")
print("  FIFO - First In First Out")
print("  Primero en entrar, primero en salir")

print("\nOperaciones:")
print("  enqueue() - Agregar al final")
print("  dequeue() - Eliminar del inicio")
print("  front() - Ver primero sin eliminar")
print("  is_empty() - Verificar si vacía")

print("\nUsos:")
print("  ✅ Procesamiento de tareas")
print("  ✅ BFS (Breadth-First Search)")
print("  ✅ Buffers")
print("  ✅ Scheduling")

print("\n" + "=" * 50)
