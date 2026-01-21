"""
DICCIONARIO: CREAR
==================
Crear diccionarios en Python
"""

print("=" * 50)
print("CREAR DICCIONARIOS")
print("=" * 50)

# Crear diccionario vacío
diccionario_vacio = {}
print(f"\nDiccionario vacío: {diccionario_vacio}")

# Crear diccionario con elementos
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(f"Diccionario: {persona}")

# Crear con dict()
persona2 = dict(nombre="María", edad=25, ciudad="Barcelona")
print(f"Con dict(): {persona2}")

# Crear desde lista de tuplas
persona3 = dict([("nombre", "Pedro"), ("edad", 28)])
print(f"Desde lista de tuplas: {persona3}")

print("\n" + "=" * 50)
