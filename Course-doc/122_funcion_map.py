"""
FUNCIÓN: MAP
============
Aplicar una función a cada elemento de una secuencia
"""

print("=" * 50)
print("FUNCIÓN MAP()")
print("=" * 50)

# map() básico
numeros = [1, 2, 3, 4, 5]
print(f"\nLista: {numeros}")

# Con función normal
def cuadrado(x):
    return x ** 2

cuadrados = list(map(cuadrado, numeros))
print(f"\nCon función normal:")
print(f"  map(cuadrado, numeros) = {cuadrados}")

# Con lambda
cuadrados2 = list(map(lambda x: x ** 2, numeros))
print(f"\nCon lambda:")
print(f"  map(lambda x: x**2, numeros) = {cuadrados2}")

# Múltiples listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
sumas = list(map(lambda x, y: x + y, lista1, lista2))
print(f"\nMúltiples listas:")
print(f"  lista1 = {lista1}, lista2 = {lista2}")
print(f"  map(lambda x, y: x+y, lista1, lista2) = {sumas}")

print("\n" + "=" * 50)
