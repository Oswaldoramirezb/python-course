"""
DICCIONARIO: MÉTODOS
====================
Métodos útiles de diccionarios
"""

print("=" * 50)
print("MÉTODOS DE DICCIONARIOS")
print("=" * 50)

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(f"\nDiccionario: {persona}")

print(f"\nMétodos principales:")
print(f"  keys()   → {list(persona.keys())} (todas las claves)")
print(f"  values() → {list(persona.values())} (todos los valores)")
print(f"  items()  → {list(persona.items())} (pares clave-valor)")

# Iterar
print(f"\nIterar sobre diccionario:")
for clave in persona:
    print(f"  {clave}: {persona[clave]}")

print(f"\nIterar con items():")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

print("\n" + "=" * 50)
