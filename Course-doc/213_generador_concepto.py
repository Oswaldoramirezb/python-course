"""
GENERADOR: CONCEPTO
===================
¿Qué es un generador?
"""

print("=" * 50)
print("CONCEPTO DE GENERADORES")
print("=" * 50)

print("\nGenerador:")
print("  - Función que retorna un iterador")
print("  - Usa 'yield' en lugar de 'return'")
print("  - Genera valores uno a uno (lazy evaluation)")

print("\nVentajas:")
print("  ✅ Eficiencia de memoria")
print("  ✅ Generación bajo demanda")
print("  ✅ Puede ser infinito")

print("\nComparación:")
print("  Función normal:")
print("    def numeros():")
print("        return [1, 2, 3, 4, 5]  # Crea lista completa")
print("")
print("  Generador:")
print("    def numeros():")
print("        yield 1")
print("        yield 2")
print("        yield 3  # Genera uno a uno")

print("\nEjemplo:")
print("  def contar_hasta(n):")
print("      i = 1")
print("      while i <= n:")
print("          yield i")
print("          i += 1")
print("")
print("  for numero in contar_hasta(5):")
print("      print(numero)")

print("\nUso:")
print("  - Iterar sobre secuencias grandes")
print("  - Procesar datos en streaming")
print("  - Crear iteradores personalizados")

print("\n" + "=" * 50)
