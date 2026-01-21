"""
RESUMEN: CONTEXT MANAGERS
=========================
Todas las operaciones con context managers
"""

print("=" * 50)
print("RESUMEN - CONTEXT MANAGERS")
print("=" * 50)

print("\nConcepto:")
print("  - Objeto que maneja recursos")
print("  - Se usa con 'with' statement")
print("  - Garantiza limpieza automática")

print("\nSintaxis:")
print("  with contexto as variable:")
print("      # código")
print("  # Limpieza automática")

print("\nCrear context manager:")
print("  Como clase:")
print("    class MiContexto:")
print("        def __enter__(self): ...")
print("        def __exit__(self, ...): ...")
print("")
print("  Con decorador:")
print("    @contextmanager")
print("    def mi_contexto():")
print("        yield valor")

print("\nProtocolo:")
print("  __enter__() - Se ejecuta al entrar")
print("  __exit__() - Se ejecuta al salir")

print("\nUsos comunes:")
print("  ✅ Archivos")
print("  ✅ Conexiones de base de datos")
print("  ✅ Locks (threading)")
print("  ✅ Recursos temporales")

print("\nVentajas:")
print("  ✅ Limpieza automática")
print("  ✅ Manejo de errores")
print("  ✅ Código más limpio")

print("\n" + "=" * 50)
