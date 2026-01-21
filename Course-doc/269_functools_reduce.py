"""
FUNCTOOLS: REDUCE
================
Reducir secuencia a un valor
"""

print("=" * 50)
print("REDUCE")
print("=" * 50)

from functools import reduce

# reduce() básico
numeros = [1, 2, 3, 4, 5]

suma = reduce(lambda x, y: x + y, numeros)
print(f"\nReducir a suma:")
print(f"  numeros = {numeros}")
print(f"  reduce(lambda x, y: x + y, numeros) = {suma}")

# Con valor inicial
producto = reduce(lambda x, y: x * y, numeros, 1)
print(f"\nReducir a producto:")
print(f"  reduce(lambda x, y: x * y, numeros, 1) = {producto}")

# Máximo
maximo = reduce(lambda x, y: x if x > y else y, numeros)
print(f"\nReducir a máximo:")
print(f"  reduce(lambda x, y: x if x > y else y, numeros) = {maximo}")

# Concatenar cadenas
palabras = ["Hola", " ", "Mundo"]
texto = reduce(lambda x, y: x + y, palabras)
print(f"\nConcatenar:")
print(f"  palabras = {palabras}")
print(f"  reduce(lambda x, y: x + y, palabras) = '{texto}'")

print("\nEquivalente a:")
print("  resultado = valor_inicial")
print("  for elemento in secuencia:")
print("      resultado = funcion(resultado, elemento)")

print("\n" + "=" * 50)
