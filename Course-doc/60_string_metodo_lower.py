"""
STRING: MÉTODO LOWER
====================
Convierte todo el texto a minúsculas
"""

print("=" * 50)
print("MÉTODO LOWER()")
print("=" * 50)

# lower() - convertir a minúsculas
texto = "PYTHON ES GENIAL"
print(f"\nTexto original: '{texto}'")

texto_minusculas = texto.lower()
print(f"Después de lower(): '{texto_minusculas}'")

# Ejemplo práctico - normalizar entrada
entrada = "MAYÚSCULAS"
print(f"\nEjemplo práctico:")
print(f"  entrada = '{entrada}'")
print(f"  entrada.lower() = '{entrada.lower()}'")

print("\n" + "=" * 50)
