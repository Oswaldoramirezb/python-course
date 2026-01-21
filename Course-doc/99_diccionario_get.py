"""
DICCIONARIO: MÉTODO GET
=======================
Obtener valores de forma segura
"""

print("=" * 50)
print("MÉTODO GET()")
print("=" * 50)

persona = {"nombre": "Juan", "edad": 30}
print(f"\nDiccionario: {persona}")

# get() básico
nombre = persona.get("nombre")
print(f"  persona.get('nombre') = {nombre}")

# get() con valor por defecto
email = persona.get("email", "No disponible")
print(f"  persona.get('email', 'No disponible') = {email}")

# Comparación: [] vs get()
print(f"\nComparación:")
print(f"  persona['nombre'] = {persona['nombre']} ✅")
print(f"  persona['email'] → KeyError ❌")
print(f"  persona.get('email') = {persona.get('email')} ✅ (None)")
print(f"  persona.get('email', 'default') = {persona.get('email', 'default')} ✅")

print("\n" + "=" * 50)
