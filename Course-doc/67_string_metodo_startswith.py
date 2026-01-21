"""
STRING: MÉTODO STARTWITH
=========================
Verifica si el texto comienza con algo
"""

print("=" * 50)
print("MÉTODO STARTWITH()")
print("=" * 50)

# startswith() - verificar inicio
texto = "Python es genial"
print(f"\nTexto: '{texto}'")

resultado = texto.startswith("Python")
print(f"startswith('Python') = {resultado}")

resultado2 = texto.startswith("Java")
print(f"startswith('Java') = {resultado2}")

# Ejemplo práctico
archivo = "documento.pdf"
print(f"\nEjemplo práctico:")
print(f"  archivo = '{archivo}'")
if archivo.startswith("documento"):
    print(f"  ✅ El archivo comienza con 'documento'")

print("\n" + "=" * 50)
