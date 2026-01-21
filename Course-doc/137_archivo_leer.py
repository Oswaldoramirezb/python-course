"""
ARCHIVO: LEER
=============
Leer contenido de archivos
"""

print("=" * 50)
print("LEER ARCHIVOS")
print("=" * 50)

# Crear archivo de ejemplo
with open("ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("Línea 1\nLínea 2\nLínea 3\nLínea 4")

# read() - leer todo
print("\nread() - leer todo:")
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(f"  {contenido}")

# readline() - leer una línea
print("\nreadline() - leer una línea:")
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    linea = archivo.readline()
    print(f"  Primera línea: {linea.strip()}")

# readlines() - leer todas las líneas
print("\nreadlines() - leer todas las líneas:")
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print(f"  {lineas}")

# Iterar sobre líneas
print("\nIterar sobre líneas:")
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    for i, linea in enumerate(archivo, 1):
        print(f"  Línea {i}: {linea.strip()}")

print("\n" + "=" * 50)
