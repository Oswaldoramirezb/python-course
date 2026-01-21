"""
STRING: MÉTODO COUNT
====================
Cuenta cuántas veces aparece un texto
"""

print("=" * 50)
print("MÉTODO COUNT()")
print("=" * 50)

# count() - contar ocurrencias
texto = "Python es genial, Python es fácil"
print(f"\nTexto: '{texto}'")

cantidad = texto.count("Python")
print(f"count('Python') = {cantidad}")

# count() con caracteres
texto2 = "programación"
print(f"\nContar caracteres:")
print(f"  '{texto2}'")
cantidad2 = texto2.count("a")
print(f"  count('a') = {cantidad2}")

print("\n" + "=" * 50)
