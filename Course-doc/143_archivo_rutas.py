"""
ARCHIVO: RUTAS
==============
Trabajar con rutas de archivos
"""

print("=" * 50)
print("RUTAS DE ARCHIVOS")
print("=" * 50)

import os

# Obtener ruta actual
ruta_actual = os.getcwd()
print(f"\nRuta actual: {ruta_actual}")

# Unir rutas
ruta_archivo = os.path.join("carpeta", "archivo.txt")
print(f"\nUnir rutas:")
print(f"  os.path.join('carpeta', 'archivo.txt') = {ruta_archivo}")

# Obtener directorio y nombre
ruta = "/home/usuario/documentos/archivo.txt"
directorio = os.path.dirname(ruta)
nombre_archivo = os.path.basename(ruta)
print(f"\nSeparar ruta:")
print(f"  ruta = '{ruta}'")
print(f"  os.path.dirname(ruta) = {directorio}")
print(f"  os.path.basename(ruta) = {nombre_archivo}")

# Obtener extensión
nombre, extension = os.path.splitext("archivo.txt")
print(f"\nSeparar extensión:")
print(f"  os.path.splitext('archivo.txt') = ('{nombre}', '{extension}')")

# Ruta absoluta
ruta_absoluta = os.path.abspath("ejemplo.txt")
print(f"\nRuta absoluta:")
print(f"  os.path.abspath('ejemplo.txt') = {ruta_absoluta}")

print("\n" + "=" * 50)
