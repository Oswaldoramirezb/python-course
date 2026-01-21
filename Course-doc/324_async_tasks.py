"""
ASYNC/AWAIT: TASKS
==================
Crear y manejar tareas asíncronas
"""

print("=" * 50)
print("TASKS - TAREAS ASÍNCRONAS")
print("=" * 50)

import asyncio

# Crear tarea
async def tarea(nombre, tiempo):
    """Tarea asíncrona"""
    print(f"  Iniciando {nombre}...")
    await asyncio.sleep(tiempo)
    print(f"  {nombre} completado")
    return f"Resultado de {nombre}"

print("\nCrear tarea:")
print("  task = asyncio.create_task(tarea('Tarea 1', 1))")
print("  resultado = await task")

# Ejecutar múltiples tareas
async def ejecutar_tareas():
    """Ejecutar múltiples tareas"""
    print("\nCrear múltiples tareas:")
    task1 = asyncio.create_task(tarea("Tarea 1", 0.1))
    task2 = asyncio.create_task(tarea("Tarea 2", 0.1))
    task3 = asyncio.create_task(tarea("Tarea 3", 0.1))
    
    # Esperar todas
    resultados = await asyncio.gather(task1, task2, task3)
    return resultados

print("\nEjecutar tareas:")
asyncio.run(ejecutar_tareas())

# Tareas con timeout
async def tarea_con_timeout():
    """Tarea con timeout"""
    try:
        await asyncio.wait_for(tarea("Tarea larga", 2), timeout=1.0)
    except asyncio.TimeoutError:
        print("  ⚠️  Tarea excedió el timeout")

print("\nTarea con timeout:")
print("  await asyncio.wait_for(tarea(), timeout=1.0)")

print("\nMétodos de tasks:")
print("  task.cancel() - Cancelar tarea")
print("  task.done() - Verificar si completó")
print("  task.result() - Obtener resultado")

print("\nVentajas:")
print("  ✅ Ejecución concurrente")
print("  ✅ Control de tareas")
print("  ✅ Timeouts y cancelación")

print("\n" + "=" * 50)
