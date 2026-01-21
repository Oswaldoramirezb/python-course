"""
RESUMEN: ENUMERACIONES
======================
Todas las operaciones con enumeraciones
"""

print("=" * 50)
print("RESUMEN - ENUMERACIONES")
print("=" * 50)

print("\nConcepto:")
print("  - Conjunto de constantes con nombre")
print("  - Valores fijos y predefinidos")

print("\nSintaxis básica:")
print("  from enum import Enum")
print("")
print("  class MiEnum(Enum):")
print("      VALOR1 = 1")
print("      VALOR2 = 2")

print("\nTipos:")
print("  Enum - Básico")
print("  IntEnum - Comparable con enteros")
print("  Flag - Para combinaciones de valores")

print("\nOperaciones:")
print("  MiEnum.VALOR1 - Acceder")
print("  MiEnum.VALOR1.name - Nombre")
print("  MiEnum.VALOR1.value - Valor")
print("  list(MiEnum) - Listar todos")

print("\nCon auto():")
print("  class Color(Enum):")
print("      ROJO = auto()")
print("      VERDE = auto()")

print("\nVentajas:")
print("  ✅ Valores predefinidos")
print("  ✅ Evita errores")
print("  ✅ Código legible")
print("  ✅ Autocompletado")

print("\nUso:")
print("  - Estados")
print("  - Opciones")
print("  - Constantes nombradas")

print("\n" + "=" * 50)
