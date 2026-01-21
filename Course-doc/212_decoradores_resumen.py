"""
RESUMEN: DECORADORES
====================
Todas las operaciones con decoradores
"""

print("=" * 50)
print("RESUMEN - DECORADORES")
print("=" * 50)

print("\nConcepto:")
print("  - Función que modifica otra función")
print("  - Sintaxis: @decorador")

print("\nTipos:")
print("  - Decorador básico")
print("  - Decorador con argumentos")
print("  - Decorador con parámetros")
print("  - Decorador de clase")

print("\nSintaxis:")
print("  @decorador")
print("  def funcion():")
print("      pass")

print("\nDecorador básico:")
print("  def decorador(func):")
print("      def wrapper():")
print("          func()")
print("      return wrapper")

print("\nDecorador con parámetros:")
print("  def decorador(param):")
print("      def decorador_real(func):")
print("          ...")
print("      return decorador_real")

print("\nBuilt-in:")
print("  @staticmethod, @classmethod, @property")
print("  @functools.lru_cache, @functools.wraps")

print("\nUsos comunes:")
print("  ✅ Medir tiempo")
print("  ✅ Logging")
print("  ✅ Validación")
print("  ✅ Cache")
print("  ✅ Autenticación")

print("\n" + "=" * 50)
