"""
ARCHIVO: VERIFICAR EXISTENCIA
=============================
Verificar si un archivo existe
"""

print("=" * 50)
print("VERIFICAR SI ARCHIVO EXISTE")
print("=" * 50)

import os

# os.path.exists()
archivo = "ejemplo.txt"
existe = os.path.exists(archivo)
print(f"\nos.path.exists():")
print(f"  os.path.exists('{archivo}') = {existe}")

# os.path.isfile() - verificar si es archivo
es_archivo = os.path.isfile(archivo)
print(f"\nos.path.isfile():")
print(f"  os.path.isfile('{archivo}') = {es_archivo}")

# os.path.isdir() - verificar si es directorio
es_directorio = os.path.isdir("course-cursor")
print(f"\nos.path.isdir():")
print(f"  os.path.isdir('course-cursor') = {es_directorio}")

# Obtener tamaño
if existe:
    tamaño = os.path.getsize(archivo)
    print(f"\nTamaño del archivo:")
    print(f"  os.path.getsize('{archivo}') = {tamaño} bytes")

# Listar archivos en directorio
print(f"\nListar archivos:")
archivos = [f for f in os.listdir(".") if os.path.isfile(f)]
print(f"  Archivos en directorio actual: {len(archivos)} archivos")

print("\n" + "=" * 50)
