"""
DATACLASS: CONCEPTO
===================
¿Qué es una dataclass?
"""

print("=" * 50)
print("CONCEPTO DE DATACLASS")
print("=" * 50)

print("\nDataclass:")
print("  - Decorador que simplifica clases de datos")
print("  - Genera automáticamente métodos comunes")
print("  - Menos código boilerplate")

print("\nMétodos generados automáticamente:")
print("  ✅ __init__()")
print("  ✅ __repr__()")
print("  ✅ __eq__()")
print("  ✅ __hash__() (opcional)")

print("\nEjemplo comparación:")
print("  Clase normal:")
print("    class Persona:")
print("        def __init__(self, nombre, edad):")
print("            self.nombre = nombre")
print("            self.edad = edad")
print("        def __repr__(self): ...")
print("        def __eq__(self, otro): ...")
print("")
print("  Con dataclass:")
print("    @dataclass")
print("    class Persona:")
print("        nombre: str")
print("        edad: int")

print("\nVentajas:")
print("  ✅ Menos código")
print("  ✅ Más legible")
print("  ✅ Métodos automáticos")
print("  ✅ Type hints integrados")

print("\nUso:")
print("  - Clases que principalmente almacenan datos")
print("  - Reducir código repetitivo")
print("  - Mejorar legibilidad")

print("\n" + "=" * 50)
