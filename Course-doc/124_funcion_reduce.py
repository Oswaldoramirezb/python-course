"""
FUNCIÓN: REDUCE
===============
Reducir una secuencia a un solo valor
"""

print("=" * 50)
print("FUNCIÓN REDUCE()")
print("=" * 50)

from functools import reduce

# reduce() básico - suma
numeros = [1, 2, 3, 4, 5]
print(f"\nLista: {numeros}")

suma = reduce(lambda x, y: x + y, numeros)
print(f"\nSuma con reduce:")
print(f"  reduce(lambda x, y: x+y, numeros) = {suma}")

# Multiplicación
producto = reduce(lambda x, y: x * y, numeros)
print(f"\nProducto con reduce:")
print(f"  reduce(lambda x, y: x*y, numeros) = {producto}")

# Máximo
maximo = reduce(lambda x, y: x if x > y else y, numeros)
print(f"\nMáximo con reduce:")
print(f"  reduce(lambda x, y: x if x>y else y, numeros) = {maximo}")

# Con valor inicial
suma_inicial = reduce(lambda x, y: x + y, numeros, 10)
print(f"\nCon valor inicial 10:")
print(f"  reduce(lambda x, y: x+y, numeros, 10) = {suma_inicial}")

print("\n" + "=" * 50)
