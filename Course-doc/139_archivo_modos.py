"""
ARCHIVO: MODOS
==============
Diferentes modos de apertura de archivos
"""

print("=" * 50)
print("MODOS DE APERTURA DE ARCHIVOS")
print("=" * 50)

print("\nModos básicos:")
print("  'r'  - Lectura (read)")
print("  'w'  - Escritura (write) - sobrescribe si existe")
print("  'a'  - Agregar (append) - agrega al final")
print("  'x'  - Crear - error si ya existe")

print("\nModos combinados:")
print("  'r+' - Lectura y escritura")
print("  'w+' - Escritura y lectura (sobrescribe)")
print("  'a+' - Agregar y lectura")

print("\nModos binarios:")
print("  'rb' - Lectura binaria")
print("  'wb' - Escritura binaria")
print("  'ab' - Agregar binario")

# Ejemplo con modo 'a' (append)
print("\nEjemplo con modo 'a' (append):")
with open("ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("Línea inicial\n")

with open("ejemplo.txt", "a", encoding="utf-8") as f:
    f.write("Línea agregada\n")
    print("  ✅ Línea agregada sin sobrescribir")

print("\n" + "=" * 50)
