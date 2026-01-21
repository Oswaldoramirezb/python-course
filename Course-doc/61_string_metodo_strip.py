"""
STRING: MÉTODO STRIP
=====================
Elimina espacios en blanco al inicio y final
"""

print("=" * 50)
print("MÉTODO STRIP()")
print("=" * 50)

# strip() - eliminar espacios
texto = "   Python   "
print(f"\nTexto original: '{texto}' (tiene espacios)")

texto_limpio = texto.strip()
print(f"Después de strip(): '{texto_limpio}'")

# lstrip() - eliminar solo a la izquierda
texto2 = "   Python"
print(f"\nlstrip() - solo izquierda:")
print(f"  '{texto2}' → '{texto2.lstrip()}'")

# rstrip() - eliminar solo a la derecha
texto3 = "Python   "
print(f"\nrstrip() - solo derecha:")
print(f"  '{texto3}' → '{texto3.rstrip()}'")

print("\n" + "=" * 50)
