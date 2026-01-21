"""
DECORADOR: CONCEPTO
===================
¿Qué es un decorador?
"""

print("=" * 50)
print("CONCEPTO DE DECORADORES")
print("=" * 50)

print("\nDecorador:")
print("  - Función que modifica otra función")
print("  - Agrega funcionalidad sin modificar el código original")
print("  - Sintaxis: @decorador")

print("\nEjemplo visual:")
print("  @mi_decorador")
print("  def mi_funcion():")
print("      pass")
print("")
print("  Es equivalente a:")
print("  def mi_funcion():")
print("      pass")
print("  mi_funcion = mi_decorador(mi_funcion)")

print("\nUsos comunes:")
print("  ✅ Medir tiempo de ejecución")
print("  ✅ Logging")
print("  ✅ Validación")
print("  ✅ Cache")
print("  ✅ Autenticación")

print("\nVentajas:")
print("  ✅ Código más limpio")
print("  ✅ Reutilización")
print("  ✅ Separación de responsabilidades")

print("\nEjemplo simple:")
print("  def decorador(func):")
print("      def wrapper():")
print("          print('Antes')")
print("          func()")
print("          print('Después')")
print("      return wrapper")

print("\n" + "=" * 50)
