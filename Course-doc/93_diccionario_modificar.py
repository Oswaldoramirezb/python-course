"""
DICCIONARIO: MODIFICAR
======================
Modificar y agregar elementos
"""

print("=" * 50)
print("MODIFICAR DICCIONARIOS")
print("=" * 50)

persona = {"nombre": "Juan", "edad": 30}
print(f"\nDiccionario original: {persona}")

# Modificar valor existente
persona["edad"] = 31
print(f"Después de persona['edad'] = 31: {persona}")

# Agregar nuevo elemento
persona["ciudad"] = "Madrid"
print(f"Después de persona['ciudad'] = 'Madrid': {persona}")

# Actualizar múltiples valores
persona.update({"email": "juan@email.com", "telefono": "123456"})
print(f"Después de update(): {persona}")

print("\n" + "=" * 50)
