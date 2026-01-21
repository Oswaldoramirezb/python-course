"""
CONTEXT MANAGER: CON DECORADOR
===============================
Crear context manager con @contextmanager
"""

print("=" * 50)
print("CONTEXT MANAGER CON DECORADOR")
print("=" * 50)

from contextlib import contextmanager

# Context manager con decorador
@contextmanager
def archivo_temporal(contenido):
    """Context manager creado con decorador"""
    # Código antes (__enter__)
    nombre_archivo = "temp.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"  ✅ Archivo temporal creado")
    
    try:
        # yield separa __enter__ de __exit__
        yield nombre_archivo
    finally:
        # Código después (__exit__)
        import os
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)
            print(f"  ✅ Archivo temporal eliminado")

print("\nContext manager con @contextmanager:")
print("  @contextmanager")
print("  def mi_contexto():")
print("      # Código antes")
print("      yield valor")
print("      # Código después")

print("\nUsar:")
with archivo_temporal("Contenido temporal") as archivo:
    with open(archivo, "r", encoding="utf-8") as f:
        print(f"  Contenido: {f.read()}")

print("\nVentajas del decorador:")
print("  ✅ Menos código")
print("  ✅ Más simple")
print("  ✅ Útil para context managers simples")

print("\n" + "=" * 50)
