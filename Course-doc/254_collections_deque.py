"""
COLLECTIONS: DEQUE
=================
Cola de doble extremo (double-ended queue)
"""

print("=" * 50)
print("DEQUE - COLA DE DOBLE EXTREMO")
print("=" * 50)

from collections import deque

# Crear deque
cola = deque([1, 2, 3])
print(f"\nDeque: {cola}")

# Agregar al final
cola.append(4)
print(f"\nappend(4) al final: {cola}")

# Agregar al inicio
cola.appendleft(0)
print(f"appendleft(0) al inicio: {cola}")

# Eliminar del final
elemento = cola.pop()
print(f"\npop() del final: {elemento}, deque: {cola}")

# Eliminar del inicio
elemento2 = cola.popleft()
print(f"popleft() del inicio: {elemento2}, deque: {cola}")

print("\nVentajas sobre list:")
print("  ✅ append/pop O(1) en ambos extremos")
print("  ✅ Más eficiente para colas")
print("  ✅ Útil para stacks y queues")

print("\n" + "=" * 50)
