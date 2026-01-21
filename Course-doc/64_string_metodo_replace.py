"""
STRING: MÉTODO REPLACE
======================
Reemplaza parte del texto
"""

print("=" * 50)
print("MÉTODO REPLACE()")
print("=" * 50)

# replace() - reemplazar texto
texto = "Python es genial"
print(f"\nTexto original: '{texto}'")

texto_nuevo = texto.replace("genial", "fantástico")
print(f"Después de replace('genial', 'fantástico'): '{texto_nuevo}'")

# replace() con límite
texto2 = "hola hola hola"
print(f"\nCon límite de reemplazos:")
print(f"  '{texto2}'")
texto3 = texto2.replace("hola", "adiós", 2)
print(f"  replace('hola', 'adiós', 2) = '{texto3}'")

print("\n" + "=" * 50)
