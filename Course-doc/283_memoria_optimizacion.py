"""
MEMORIA: OPTIMIZACIÓN
=====================
Técnicas para optimizar uso de memoria
"""

print("=" * 50)
print("OPTIMIZACIÓN DE MEMORIA")
print("=" * 50)

import sys

# 1. Usar generadores en lugar de listas
print("\n1. Usar generadores:")
print("  Lista: [x**2 for x in range(1000)]  # Todos en memoria")
print("  Generador: (x**2 for x in range(1000))  # Uno a uno")

lista = [x**2 for x in range(1000)]
generador = (x**2 for x in range(1000))

print(f"  sys.getsizeof(lista) = {sys.getsizeof(lista)} bytes")
print(f"  sys.getsizeof(generador) = {sys.getsizeof(generador)} bytes")

# 2. Eliminar referencias innecesarias
print("\n2. Eliminar referencias:")
print("  del variable  # Libera referencia")
print("  variable = None  # También libera")

# 3. Usar __slots__ en clases
class ConSlots:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SinSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj_slots = ConSlots(1, 2)
obj_sin = SinSlots(1, 2)

print("\n3. Usar __slots__:")
print(f"  sys.getsizeof(obj_slots) = {sys.getsizeof(obj_slots)} bytes")
print(f"  sys.getsizeof(obj_sin) = {sys.getsizeof(obj_sin)} bytes")

# 4. Reutilizar objetos
print("\n4. Reutilizar objetos:")
print("  - Evitar crear objetos innecesarios")
print("  - Usar objetos inmutables cuando sea posible")

print("\nTécnicas:")
print("  ✅ Generadores para secuencias grandes")
print("  ✅ __slots__ para clases con muchos objetos")
print("  ✅ Eliminar referencias innecesarias")
print("  ✅ Reutilizar objetos")

print("\n" + "=" * 50)
