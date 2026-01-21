"""
FUNCIÓN: ENUMERATE
==================
Obtener índice y valor al iterar
"""

print("=" * 50)
print("FUNCIÓN ENUMERATE()")
print("=" * 50)

# enumerate() básico
frutas = ["manzana", "banana", "naranja"]
print(f"\nLista: {frutas}")

# Con enumerate
print(f"\nCon enumerate():")
for indice, fruta in enumerate(frutas):
    print(f"  Índice {indice}: {fruta}")

# Con inicio personalizado
print(f"\nCon start=1:")
for indice, fruta in enumerate(frutas, start=1):
    print(f"  Posición {indice}: {fruta}")

# Convertir a lista
lista_enumerada = list(enumerate(frutas))
print(f"\nConvertir a lista:")
print(f"  list(enumerate(frutas)) = {lista_enumerada}")

# Útil para crear listas numeradas
tareas = ["Estudiar", "Ejercicio", "Comer"]
print(f"\nLista numerada:")
for i, tarea in enumerate(tareas, 1):
    print(f"  {i}. {tarea}")

print("\n" + "=" * 50)
