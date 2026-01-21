"""
ASYNC/AWAIT: AWAIT
==================
Usar await para esperar resultados
"""

print("=" * 50)
print("AWAIT - ESPERAR RESULTADOS")
print("=" * 50)

import asyncio

# Función asíncrona que simula I/O
async def obtener_datos(tiempo, nombre):
    """Simula operación I/O"""
    print(f"  Iniciando {nombre}...")
    await asyncio.sleep(tiempo)
    print(f"  {nombre} completado")
    return f"Datos de {nombre}"

print("\nUsar await:")
print("  async def mi_funcion():")
print("      resultado = await otra_funcion()")
print("      return resultado")

# Ejemplo secuencial (lento)
async def secuencial():
    """Ejecutar tareas secuencialmente"""
    print("\nEjecución secuencial:")
    dato1 = await obtener_datos(0.1, "Tarea 1")
    dato2 = await obtener_datos(0.1, "Tarea 2")
    return dato1, dato2

# Ejemplo concurrente (rápido)
async def concurrente():
    """Ejecutar tareas concurrentemente"""
    print("\nEjecución concurrente:")
    dato1 = obtener_datos(0.1, "Tarea 1")
    dato2 = obtener_datos(0.1, "Tarea 2")
    resultado1, resultado2 = await asyncio.gather(dato1, dato2)
    return resultado1, resultado2

print("\nComparación:")
print("  Secuencial: await tarea1(); await tarea2()")
print("  Concurrente: await asyncio.gather(tarea1(), tarea2())")

# Ejecutar ejemplo
print("\nEjecutar ejemplo:")
asyncio.run(concurrente())

print("\nVentajas de await:")
print("  ✅ No bloquea el hilo")
print("  ✅ Permite otras tareas")
print("  ✅ Eficiente para I/O")

print("\n" + "=" * 50)
