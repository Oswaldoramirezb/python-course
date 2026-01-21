"""
ARCHIVO: ESCRIBIR
=================
Escribir contenido en archivos
"""

print("=" * 50)
print("ESCRIBIR ARCHIVOS")
print("=" * 50)

# write() - escribir texto
print("\nwrite() - escribir texto:")
with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Este es un nuevo archivo.\n")
    archivo.write("Python es genial para manejar archivos.")
    print("  ✅ Archivo escrito")

# writelines() - escribir múltiples líneas
print("\nwritelines() - escribir múltiples líneas:")
lineas = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]
with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)
    print("  ✅ Líneas escritas")

# append() - agregar al final
print("\nappend() - agregar al final:")
with open("ejemplo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\nLínea agregada")
    print("  ✅ Línea agregada")

# Leer para verificar
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    print(f"\n  Contenido final:")
    print(f"  {archivo.read()}")

print("\n" + "=" * 50)
