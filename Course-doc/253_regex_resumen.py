"""
RESUMEN: EXPRESIONES REGULARES
===============================
Todas las operaciones con regex
"""

print("=" * 50)
print("RESUMEN - REGEX")
print("=" * 50)

print("\nImportar:")
print("  import re")

print("\nFunciones principales:")
print("  re.match() - Busca al inicio")
print("  re.search() - Busca en cualquier parte")
print("  re.findall() - Encuentra todas")
print("  re.sub() - Reemplaza")

print("\nCaracteres especiales:")
print("  . - Cualquier carácter")
print("  \\d - Dígito (0-9)")
print("  \\w - Letra, número o _")
print("  \\s - Espacio en blanco")
print("  ^ - Inicio de cadena")
print("  $ - Fin de cadena")

print("\nCuantificadores:")
print("  + - Uno o más")
print("  * - Cero o más")
print("  ? - Cero o uno")
print("  {n} - Exactamente n veces")
print("  {n,m} - Entre n y m veces")

print("\nEjemplos:")
print("  r'\\d+' - Uno o más dígitos")
print("  r'\\w+@\\w+\\.\\w+' - Email simple")
print("  r'^\\d{3}-\\d{3}-\\d{4}$' - Teléfono")

print("\nUsos:")
print("  ✅ Validación")
print("  ✅ Búsqueda")
print("  ✅ Extracción")
print("  ✅ Reemplazo")

print("\n" + "=" * 50)
