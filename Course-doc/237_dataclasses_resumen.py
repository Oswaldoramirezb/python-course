"""
RESUMEN: DATACLASSES
====================
Todas las operaciones con dataclasses
"""

print("=" * 50)
print("RESUMEN - DATACLASSES")
print("=" * 50)

print("\nConcepto:")
print("  - Decorador que simplifica clases de datos")
print("  - Genera métodos automáticamente")

print("\nSintaxis básica:")
print("  @dataclass")
print("  class Persona:")
print("      nombre: str")
print("      edad: int")

print("\nMétodos generados:")
print("  ✅ __init__()")
print("  ✅ __repr__()")
print("  ✅ __eq__()")
print("  ✅ __hash__() (opcional)")

print("\nOpciones:")
print("  @dataclass(frozen=True) - Inmutable")
print("  @dataclass(order=True) - Permite ordenar")
print("  field() - Configuración avanzada")

print("\nVentajas:")
print("  ✅ Menos código")
print("  ✅ Más legible")
print("  ✅ Type hints integrados")
print("  ✅ Métodos automáticos")

print("\nUso:")
print("  - Clases que almacenan datos")
print("  - Reducir código repetitivo")
print("  - Mejorar legibilidad")

print("\nComparación:")
print("  Clase normal: ~20 líneas")
print("  Dataclass: ~5 líneas")

print("\n" + "=" * 50)
