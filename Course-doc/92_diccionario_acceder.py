"""
DICCIONARIO: ACCEDER A ELEMENTOS
=================================
Obtener valores de un diccionario
"""

print("=" * 50)
print("ACCEDER A ELEMENTOS DE DICCIONARIO")
print("=" * 50)

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(f"\nDiccionario: {persona}")

# Acceder con []
print(f"  persona['nombre'] = {persona['nombre']}")
print(f"  persona['edad'] = {persona['edad']}")

# Acceder con get() (más seguro)
print(f"\nCon get() (más seguro):")
print(f"  persona.get('nombre') = {persona.get('nombre')}")
print(f"  persona.get('email', 'No disponible') = {persona.get('email', 'No disponible')}")

# ⚠️ Error si la clave no existe
print(f"\n⚠️  Si la clave no existe:")
print(f"  persona['email'] → KeyError")
print(f"  persona.get('email') → None (sin error)")

print("\n" + "=" * 50)
