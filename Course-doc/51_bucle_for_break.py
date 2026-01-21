"""
BUCLE FOR: BREAK
================
Salir del bucle antes de que termine
"""

print("=" * 50)
print("BUCLE FOR CON BREAK")
print("=" * 50)

# Break básico
print("\nEjemplo 1 - Salir cuando encuentre 5:")
for i in range(10):
    if i == 5:
        print(f"  Encontré {i}, saliendo...")
        break
    print(f"  i = {i}")

# Buscar elemento
print("\nEjemplo 2 - Buscar en lista:")
numeros = [1, 3, 5, 7, 9, 11]
buscar = 7
print(f"  Buscando {buscar} en {numeros}")
for num in numeros:
    if num == buscar:
        print(f"  ✅ Encontrado: {num}")
        break
    print(f"  Revisando: {num}")

print("\n" + "=" * 50)
