"""
STRING: MÉTODO ENDSWITH
========================
Verifica si el texto termina con algo
"""

print("=" * 50)
print("MÉTODO ENDSWITH()")
print("=" * 50)

# endswith() - verificar final
texto = "archivo.py"
print(f"\nTexto: '{texto}'")

resultado = texto.endswith(".py")
print(f"endswith('.py') = {resultado}")

resultado2 = texto.endswith(".txt")
print(f"endswith('.txt') = {resultado2}")

# Ejemplo práctico - verificar extensión
archivo = "documento.pdf"
print(f"\nEjemplo práctico:")
print(f"  archivo = '{archivo}'")
if archivo.endswith(".pdf"):
    print(f"  ✅ Es un archivo PDF")

print("\n" + "=" * 50)
