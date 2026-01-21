"""
ARCHIVO: WITH STATEMENT
========================
Usar 'with' para manejo seguro de archivos
"""

print("=" * 50)
print("WITH STATEMENT")
print("=" * 50)

# Sin with (menos seguro)
print("\nSin with (menos seguro):")
print("  archivo = open('ejemplo.txt', 'r')")
print("  contenido = archivo.read()")
print("  archivo.close()  # ⚠️ Puede olvidarse")

# Con with (recomendado)
print("\nCon with (recomendado):")
print("  with open('ejemplo.txt', 'r') as archivo:")
print("      contenido = archivo.read()")
print("  # Se cierra automáticamente")

# Ejemplo práctico
with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Contenido de ejemplo")
    print("\n  ✅ Archivo escrito")

with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(f"  ✅ Contenido leído: {contenido}")

print("\nVentajas de 'with':")
print("  ✅ Cierre automático")
print("  ✅ Manejo de errores")
print("  ✅ Código más limpio")

print("\n" + "=" * 50)
