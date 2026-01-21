"""
ASYNC/AWAIT: ASYNC DEF
======================
Definir funciones asíncronas
"""

print("=" * 50)
print("ASYNC DEF - FUNCIONES ASÍNCRONAS")
print("=" * 50)

import asyncio

# Función asíncrona básica
async def saludar():
    """Función asíncrona simple"""
    return "Hola"

print("\nDefinir función asíncrona:")
print("  async def saludar():")
print("      return 'Hola'")

# Función asíncrona con await
async def esperar():
    """Función que espera"""
    await asyncio.sleep(1)
    return "Esperé 1 segundo"

print("\nFunción con await:")
print("  async def esperar():")
print("      await asyncio.sleep(1)")
print("      return 'Esperé 1 segundo'")

# Ejecutar función asíncrona
print("\nEjecutar función asíncrona:")
print("  asyncio.run(saludar())")
resultado = asyncio.run(saludar())
print(f"  Resultado: {resultado}")

# Múltiples funciones
async def tarea1():
    await asyncio.sleep(0.1)
    return "Tarea 1 completada"

async def tarea2():
    await asyncio.sleep(0.1)
    return "Tarea 2 completada"

print("\nEjecutar múltiples tareas:")
print("  tarea1() y tarea2() se ejecutan concurrentemente")

async def ejecutar_tareas():
    resultado1 = await tarea1()
    resultado2 = await tarea2()
    return resultado1, resultado2

# asyncio.run(ejecutar_tareas())

print("\nCaracterísticas:")
print("  - async def define función asíncrona")
print("  - Retorna coroutine")
print("  - Debe ejecutarse con asyncio.run()")
print("  - Puede usar await dentro")

print("\n" + "=" * 50)
