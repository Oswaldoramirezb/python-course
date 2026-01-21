"""
CONTEXT MANAGER: CONCEPTO
==========================
¿Qué es un context manager?
"""

print("=" * 50)
print("CONCEPT DE CONTEXT MANAGERS")
print("=" * 50)

print("\nContext Manager:")
print("  - Objeto que maneja recursos")
print("  - Se usa con 'with' statement")
print("  - Garantiza limpieza automática")

print("\nEjemplo más común - archivos:")
print("  with open('archivo.txt', 'r') as archivo:")
print("      contenido = archivo.read()")
print("  # Archivo se cierra automáticamente")

print("\nVentajas:")
print("  ✅ Limpieza automática")
print("  ✅ Manejo de errores")
print("  ✅ Código más limpio")
print("  ✅ Garantiza que recursos se liberen")

print("\nProtocolo:")
print("  - __enter__() - Se ejecuta al entrar")
print("  - __exit__() - Se ejecuta al salir")

print("\nSintaxis:")
print("  with contexto as variable:")
print("      # código")
print("  # Limpieza automática")

print("\nUsos comunes:")
print("  ✅ Archivos")
print("  ✅ Conexiones de base de datos")
print("  ✅ Locks (threading)")
print("  ✅ Recursos temporales")

print("\n" + "=" * 50)
