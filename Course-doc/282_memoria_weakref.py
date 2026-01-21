"""
MEMORIA: WEAKREF
================
Referencias débiles
"""

print("=" * 50)
print("WEAKREF - REFERENCIAS DÉBILES")
print("=" * 50)

import weakref

# Referencia normal
class Objeto:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __repr__(self):
        return f"Objeto({self.nombre})"

obj = Objeto("test")
ref_normal = obj

print("\nReferencia normal:")
print(f"  obj = {obj}")
print(f"  ref_normal = obj")
print(f"  del obj")
del obj
print(f"  ref_normal = {ref_normal}  # Todavía existe")

# Referencia débil
obj2 = Objeto("test2")
ref_debil = weakref.ref(obj2)

print("\nReferencia débil:")
print(f"  obj2 = {obj2}")
print(f"  ref_debil = weakref.ref(obj2)")
print(f"  ref_debil() = {ref_debil()}")

print(f"\nEliminar objeto:")
del obj2
print(f"  del obj2")
print(f"  ref_debil() = {ref_debil()}  # None (objeto eliminado)")

# WeakValueDictionary
print("\nWeakValueDictionary:")
print("  - Diccionario con referencias débiles")
print("  - Se eliminan automáticamente cuando no hay referencias")

weak_dict = weakref.WeakValueDictionary()
obj3 = Objeto("test3")
weak_dict["clave"] = obj3

print(f"  weak_dict['clave'] = {weak_dict.get('clave')}")
del obj3
print(f"  del obj3")
print(f"  weak_dict.get('clave') = {weak_dict.get('clave')}  # None")

print("\nUso:")
print("  ✅ Caches")
print("  ✅ Callbacks")
print("  ✅ Evitar ciclos de referencias")

print("\n" + "=" * 50)
