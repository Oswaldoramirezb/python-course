"""
RESUMEN: DICCIONARIOS
=====================
Todas las operaciones importantes con diccionarios
"""

print("=" * 50)
print("RESUMEN - DICCIONARIOS")
print("=" * 50)

persona = {"nombre": "Juan", "edad": 30}
print(f"\nDiccionario ejemplo: {persona}")

print(f"\nOperaciones principales:")
print(f"  Crear: persona = {{'nombre': 'Juan', 'edad': 30}}")
print(f"  Acceder: persona['nombre'] = {persona['nombre']}")
print(f"  Modificar: persona['edad'] = 31")
print(f"  Agregar: persona['ciudad'] = 'Madrid'")
print(f"  Eliminar: del persona['edad']")
print(f"  Métodos: keys(), values(), items(), get()")
print(f"  Comprehension: {{x: x**2 for x in range(5)}}")

print("\n" + "=" * 50)
