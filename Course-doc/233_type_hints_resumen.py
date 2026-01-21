"""
RESUMEN: TYPE HINTS
===================
Todas las operaciones con type hints
"""

print("=" * 50)
print("RESUMEN - TYPE HINTS")
print("=" * 50)

print("\nConcepto:")
print("  - Anotaciones que indican tipos")
print("  - Mejoran legibilidad y herramientas")
print("  - NO afectan ejecución")

print("\nSintaxis básica:")
print("  variable: tipo = valor")
print("  def funcion(param: tipo) -> tipo_retorno:")

print("\nTipos básicos:")
print("  int, float, str, bool")
print("  list[tipo], dict[clave, valor]")
print("  tuple[tipo1, tipo2]")

print("\nTipos avanzados:")
print("  Optional[tipo] - tipo o None")
print("  Union[tipo1, tipo2] - tipo1 o tipo2")
print("  Any - cualquier tipo")

print("\nEn funciones:")
print("  def sumar(a: int, b: int) -> int:")
print("      return a + b")

print("\nEn clases:")
print("  class Persona:")
print("      def __init__(self, nombre: str) -> None:")
print("          self.nombre: str = nombre")

print("\nVentajas:")
print("  ✅ Documentación automática")
print("  ✅ Mejor autocompletado")
print("  ✅ Detección temprana de errores")

print("\n⚠️  IMPORTANTE:")
print("  - Son solo anotaciones")
print("  - Python NO valida automáticamente")
print("  - Usar mypy para validación")

print("\n" + "=" * 50)
