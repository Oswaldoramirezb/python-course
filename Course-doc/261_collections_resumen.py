"""
RESUMEN: COLLECTIONS
====================
Todas las estructuras de collections
"""

print("=" * 50)
print("RESUMEN - COLLECTIONS")
print("=" * 50)

print("\nEstructuras principales:")
print("  deque - Cola de doble extremo")
print("  Counter - Contador de elementos")
print("  defaultdict - Diccionario con valor por defecto")
print("  OrderedDict - Diccionario ordenado")
print("  namedtuple - Tupla con campos nombrados")
print("  ChainMap - Combinar diccionarios")

print("\nDeque:")
print("  from collections import deque")
print("  cola = deque([1, 2, 3])")
print("  cola.appendleft(), cola.popleft()")

print("\nCounter:")
print("  from collections import Counter")
print("  contador = Counter(lista)")
print("  contador.most_common(3)")

print("\nDefaultDict:")
print("  from collections import defaultdict")
print("  dic = defaultdict(list)")
print("  dic['nuevo'] → [] (automático)")

print("\nNamedTuple:")
print("  from collections import namedtuple")
print("  Persona = namedtuple('Persona', ['nombre', 'edad'])")

print("\nVentajas:")
print("  ✅ Estructuras optimizadas")
print("  ✅ Funcionalidades especializadas")
print("  ✅ Mejor rendimiento en casos específicos")

print("\n" + "=" * 50)
