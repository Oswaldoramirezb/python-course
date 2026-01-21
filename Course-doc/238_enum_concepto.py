"""
ENUM: CONCEPTO
==============
¿Qué es una enumeración?
"""

print("=" * 50)
print("CONCEPTO DE ENUMERACIONES")
print("=" * 50)

print("\nEnumeración (Enum):")
print("  - Conjunto de constantes con nombre")
print("  - Valores fijos y predefinidos")
print("  - Mejora legibilidad y seguridad")

print("\nEjemplo:")
print("  Días de la semana:")
print("    LUNES, MARTES, MIÉRCOLES, etc.")
print("")
print("  Estados:")
print("    ACTIVO, INACTIVO, PENDIENTE")

print("\nVentajas:")
print("  ✅ Valores predefinidos")
print("  ✅ Evita errores de tipeo")
print("  ✅ Código más legible")
print("  ✅ Autocompletado en IDEs")

print("\nComparación:")
print("  Sin Enum:")
print("    estado = 'activo'  # ⚠️ Puede tener errores")
print("")
print("  Con Enum:")
print("    estado = Estado.ACTIVO  # ✅ Seguro")

print("\nSintaxis:")
print("  from enum import Enum")
print("")
print("  class MiEnum(Enum):")
print("      VALOR1 = 1")
print("      VALOR2 = 2")

print("\n" + "=" * 50)
