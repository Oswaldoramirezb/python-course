"""
CONTEXT MANAGER: WITH STATEMENT
================================
Usar 'with' para manejo seguro de recursos
"""

print("=" * 50)
print("WITH STATEMENT")
print("=" * 50)

# with con archivos
print("\nEjemplo 1 - Archivos:")
print("  with open('archivo.txt', 'r') as archivo:")
print("      contenido = archivo.read()")
print("  # Archivo se cierra automáticamente")

# Crear archivo de ejemplo
with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Contenido de ejemplo")

with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(f"\n  Contenido leído: {contenido}")

# Comparación: sin with
print("\nComparación:")
print("  Sin with:")
print("    archivo = open('archivo.txt')")
print("    contenido = archivo.read()")
print("    archivo.close()  # ⚠️ Puede olvidarse")
print("")
print("  Con with:")
print("    with open('archivo.txt') as archivo:")
print("        contenido = archivo.read()")
print("    # ✅ Se cierra automáticamente")

print("\nVentajas:")
print("  ✅ Cierre automático")
print("  ✅ Manejo de errores")
print("  ✅ Código más limpio")

print("\n" + "=" * 50)
