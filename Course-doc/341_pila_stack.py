"""
ESTRUCTURAS: PILA (STACK)
=========================
LIFO - Last In First Out
"""

print("=" * 50)
print("PILA (STACK) - LIFO")
print("=" * 50)

# Implementar pila con lista
class Pila:
    """Pila implementada con lista"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Agregar elemento"""
        self.items.append(item)
    
    def pop(self):
        """Eliminar y retornar último elemento"""
        if self.is_empty():
            raise IndexError("Pila vacía")
        return self.items.pop()
    
    def peek(self):
        """Ver último elemento sin eliminarlo"""
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        """Verificar si está vacía"""
        return len(self.items) == 0
    
    def size(self):
        """Tamaño de la pila"""
        return len(self.items)

print("\nImplementar pila:")
print("  class Pila:")
print("      def push(self, item): ...")
print("      def pop(self): ...")
print("      def peek(self): ...")

# Usar pila
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)

print(f"\nOperaciones:")
print(f"  push(1), push(2), push(3)")
print(f"  peek() = {pila.peek()}")
print(f"  pop() = {pila.pop()}")
print(f"  pop() = {pila.pop()}")
print(f"  size() = {pila.size()}")

print("\nCaracterísticas:")
print("  LIFO - Last In First Out")
print("  Último en entrar, primero en salir")

print("\nOperaciones:")
print("  push() - Agregar al final")
print("  pop() - Eliminar del final")
print("  peek() - Ver último sin eliminar")
print("  is_empty() - Verificar si vacía")

print("\nUsos:")
print("  ✅ Evaluación de expresiones")
print("  ✅ Undo/Redo")
print("  ✅ Navegación (back button)")
print("  ✅ Recursión (call stack)")

print("\n" + "=" * 50)
