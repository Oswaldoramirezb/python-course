"""
ARCHIVO: ABRIR
==============
Abrir archivos en Python
"""

print("=" * 50)
print("ABRIR ARCHIVOS")
print("=" * 50)

# Crear archivo de ejemplo primero
with open("ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("Este es un archivo de ejemplo.\nPython es genial.")

print("\nModos de apertura:")
print("  'r'  - Lectura (read)")
print("  'w'  - Escritura (write) - sobrescribe")
print("  'a'  - Agregar (append) - al final")
print("  'x'  - Crear - error si existe")
print("  'b'  - Binario")
print("  't'  - Texto (por defecto)")

# Abrir para lectura
print("\nAbrir para lectura:")
print("  archivo = open('ejemplo.txt', 'r', encoding='utf-8')")
print("  contenido = archivo.read()")
print("  archivo.close()")

# Con with (recomendado)
print("\nCon with (recomendado):")
print("  with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:")
print("      contenido = archivo.read()")
print("  # Se cierra automáticamente")

with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(f"\n  Contenido leído: {contenido[:30]}...")

print("\n" + "=" * 50)
