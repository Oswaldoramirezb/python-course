"""
REGEX: CONCEPTO
===============
¿Qué son las expresiones regulares?
"""

print("=" * 50)
print("CONCEPTO DE REGEX")
print("=" * 50)

import re

print("\nExpresiones Regulares (Regex):")
print("  - Patrones para buscar texto")
print("  - Muy potentes y flexibles")
print("  - Útiles para validación y búsqueda")

print("\nEjemplo simple:")
print("  texto = 'Mi email es usuario@email.com'")
print("  patron = r'@\\w+\\.\\w+'")
print("  resultado = re.search(patron, texto)")

texto = "Mi email es usuario@email.com"
patron = r"@\w+\.\w+"
resultado = re.search(patron, texto)
print(f"\nEjemplo práctico:")
print(f"  texto = '{texto}'")
if resultado:
    print(f"  Encontrado: {resultado.group()}")

print("\nCaracteres especiales:")
print("  . - Cualquier carácter")
print("  \\d - Dígito")
print("  \\w - Letra, número o _")
print("  \\s - Espacio en blanco")
print("  + - Uno o más")
print("  * - Cero o más")
print("  ? - Cero o uno")

print("\nUsos comunes:")
print("  ✅ Validar emails")
print("  ✅ Buscar patrones")
print("  ✅ Extraer información")
print("  ✅ Reemplazar texto")

print("\n" + "=" * 50)
