"""
RESUMEN: ASYNC/AWAIT
====================
Todas las operaciones asíncronas
"""

print("=" * 50)
print("RESUMEN - ASYNC/AWAIT")
print("=" * 50)

print("\nConcepto:")
print("  - Programación asíncrona")
print("  - Ejecutar sin bloquear")
print("  - Eficiente para I/O")

print("\nSintaxis:")
print("  async def mi_funcion():")
print("      resultado = await otra_funcion()")
print("      return resultado")

print("\nEjecutar:")
print("  asyncio.run(mi_funcion())")

print("\nOperaciones:")
print("  await - Esperar resultado")
print("  asyncio.create_task() - Crear tarea")
print("  asyncio.gather() - Ejecutar múltiples")
print("  asyncio.wait_for() - Con timeout")
print("  asyncio.sleep() - Esperar tiempo")

print("\nVentajas:")
print("  ✅ No bloquea el hilo")
print("  ✅ Eficiente para I/O")
print("  ✅ Múltiples tareas concurrentes")
print("  ✅ Mejor rendimiento")

print("\nCuándo usar:")
print("  - Operaciones de red")
print("  - Lectura/escritura de archivos")
print("  - APIs y servicios web")
print("  - Múltiples tareas concurrentes")

print("\nBibliotecas:")
print("  asyncio - Incluido en Python")
print("  aiohttp - HTTP asíncrono")
print("  asyncpg - PostgreSQL asíncrono")

print("\nComparación:")
print("  Síncrono - Bloquea hasta completar")
print("  Asíncrono - Continúa mientras espera")

print("\n" + "=" * 50)
