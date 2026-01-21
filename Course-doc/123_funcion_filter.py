"""
FUNCIÓN: FILTER
===============
Filtrar elementos de una secuencia
"""

print("=" * 50)
print("FUNCIÓN FILTER()")
print("=" * 50)

# filter() básico
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nLista: {numeros}")

# Filtrar pares con función
def es_par(x):
    return x % 2 == 0

pares = list(filter(es_par, numeros))
print(f"\nCon función:")
print(f"  filter(es_par, numeros) = {pares}")

# Filtrar pares con lambda
pares2 = list(filter(lambda x: x % 2 == 0, numeros))
print(f"\nCon lambda:")
print(f"  filter(lambda x: x%2==0, numeros) = {pares2}")

# Filtrar mayores que 5
mayores = list(filter(lambda x: x > 5, numeros))
print(f"\nMayores que 5:")
print(f"  filter(lambda x: x>5, numeros) = {mayores}")

print("\n" + "=" * 50)
