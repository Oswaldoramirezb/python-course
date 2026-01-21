"""
STRING: MÉTODO SPLIT
=====================
Divide una cadena en una lista
"""

print("=" * 50)
print("MÉTODO SPLIT()")
print("=" * 50)

# split() - dividir por espacios
texto = "Python es genial"
print(f"\nTexto original: '{texto}'")

palabras = texto.split()
print(f"Después de split(): {palabras}")

# split() con separador específico
fecha = "2024-01-15"
print(f"\nCon separador específico:")
print(f"  fecha = '{fecha}'")
partes = fecha.split("-")
print(f"  fecha.split('-') = {partes}")

# split() con límite
texto2 = "uno,dos,tres,cuatro"
print(f"\nCon límite:")
print(f"  '{texto2}'")
print(f"  split(',', 2) = {texto2.split(',', 2)}")

print("\n" + "=" * 50)
