"""
ASYNC/AWAIT: GATHER
===================
Ejecutar múltiples coroutines
"""

print("=" * 50)
print("GATHER - EJECUTAR MÚLTIPLES")
print("=" * 50)

import asyncio

# Funciones asíncronas
async def tarea1():
    await asyncio.sleep(0.1)
    return "Resultado 1"

async def tarea2():
    await asyncio.sleep(0.1)
    return "Resultado 2"

async def tarea3():
    await asyncio.sleep(0.1)
    return "Resultado 3"

print("\nasyncio.gather():")
print("  - Ejecuta múltiples coroutines")
print("  - Espera todas a completar")
print("  - Retorna lista de resultados")

# Ejecutar con gather
async def ejecutar_con_gather():
    """Ejecutar múltiples tareas"""
    resultados = await asyncio.gather(
        tarea1(),
        tarea2(),
        tarea3()
    )
    return resultados

print("\nEjemplo:")
print("  resultados = await asyncio.gather(")
print("      tarea1(),")
print("      tarea2(),")
print("      tarea3()")
print("  )")

resultados = asyncio.run(ejecutar_con_gather())
print(f"\nResultados: {resultados}")

# Con return_exceptions
async def tarea_con_error():
    raise ValueError("Error en tarea")

async def ejecutar_con_errores():
    """Ejecutar con manejo de errores"""
    resultados = await asyncio.gather(
        tarea1(),
        tarea_con_error(),
        tarea3(),
        return_exceptions=True
    )
    return resultados

print("\nCon return_exceptions=True:")
print("  - No detiene si hay error")
print("  - Retorna excepciones en resultados")

resultados_con_errores = asyncio.run(ejecutar_con_errores())
print(f"  Resultados: {resultados_con_errores}")

print("\nVentajas:")
print("  ✅ Ejecución concurrente")
print("  ✅ Esperar todas las tareas")
print("  ✅ Manejo de errores")
print("  ✅ Más eficiente que secuencial")

print("\n" + "=" * 50)
