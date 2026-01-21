"""
STRING: CONCATENACIÓN
======================
Unir cadenas de texto
"""

print("=" * 50)
print("STRING CONCATENACIÓN")
print("=" * 50)

# Concatenación con +
texto1 = "Hola"
texto2 = "Mundo"
print(f"\nCon operador +:")
print(f"  '{texto1}' + ' ' + '{texto2}' = '{texto1 + ' ' + texto2}'")

# Concatenación con join()
palabras = ["Python", "es", "genial"]
print(f"\nCon join():")
print(f"  palabras = {palabras}")
print(f"  ' '.join(palabras) = '{' '.join(palabras)}'")

# Concatenación múltiple
print(f"\nMúltiple concatenación:")
resultado = texto1 + " " + texto2 + "!"
print(f"  '{texto1}' + ' ' + '{texto2}' + '!' = '{resultado}'")

print("\n" + "=" * 50)
