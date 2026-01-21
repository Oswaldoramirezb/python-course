"""
COLLECTIONS: NAMEDTUPLE
========================
Tupla con campos nombrados
"""

print("=" * 50)
print("NAMEDTUPLE")
print("=" * 50)

from collections import namedtuple

# Crear namedtuple
Persona = namedtuple("Persona", ["nombre", "edad", "ciudad"])

print("\nCrear namedtuple:")
print("  Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])")

# Crear instancia
persona = Persona("Juan", 30, "Madrid")
print(f"\nCrear instancia:")
print(f"  persona = Persona('Juan', 30, 'Madrid')")

# Acceder por nombre
print(f"\nAcceder por nombre:")
print(f"  persona.nombre = {persona.nombre}")
print(f"  persona.edad = {persona.edad}")
print(f"  persona.ciudad = {persona.ciudad}")

# También por índice
print(f"\nTambién por índice:")
print(f"  persona[0] = {persona[0]}")
print(f"  persona[1] = {persona[1]}")

# Ventajas sobre tupla normal
print("\nVentajas sobre tupla normal:")
print("  ✅ Acceso por nombre (más legible)")
print("  ✅ Inmutable como tupla")
print("  ✅ Menos memoria que clase")

print("\n" + "=" * 50)
