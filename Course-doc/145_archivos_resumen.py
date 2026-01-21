"""
RESUMEN: MANEJO DE ARCHIVOS
===========================
Todas las operaciones con archivos
"""

print("=" * 50)
print("RESUMEN - MANEJO DE ARCHIVOS")
print("=" * 50)

print("\nAbrir archivos:")
print("  with open('archivo.txt', 'r') as archivo:")

print("\nModos:")
print("  'r' - Lectura")
print("  'w' - Escritura (sobrescribe)")
print("  'a' - Agregar")
print("  'x' - Crear")

print("\nLeer:")
print("  archivo.read() - todo el contenido")
print("  archivo.readline() - una línea")
print("  archivo.readlines() - todas las líneas")

print("\nEscribir:")
print("  archivo.write('texto')")
print("  archivo.writelines(lista)")

print("\nJSON:")
print("  json.dump(datos, archivo)")
print("  json.load(archivo)")

print("\nCSV:")
print("  csv.writer(archivo)")
print("  csv.reader(archivo)")

print("\nRutas:")
print("  os.path.join()")
print("  os.path.exists()")
print("  os.path.isfile()")

print("\n" + "=" * 50)
