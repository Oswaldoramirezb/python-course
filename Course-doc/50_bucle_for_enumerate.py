"""
BUCLE FOR: ENUMERATE
====================
Obtener índice y valor al mismo tiempo
"""

print("=" * 50)
print("BUCLE FOR CON ENUMERATE")
print("=" * 50)

# enumerate básico
print("\nEjemplo 1 - enumerate básico:")
frutas = ["manzana", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"  Posición {indice}: {fruta}")

# enumerate con inicio personalizado
print("\nEjemplo 2 - enumerate con start=1:")
for indice, fruta in enumerate(frutas, start=1):
    print(f"  Posición {indice}: {fruta}")

# Útil para crear listas numeradas
print("\nEjemplo 3 - Lista numerada:")
tareas = ["Estudiar", "Ejercicio", "Comer"]
for i, tarea in enumerate(tareas, 1):
    print(f"  {i}. {tarea}")

print("\n" + "=" * 50)
