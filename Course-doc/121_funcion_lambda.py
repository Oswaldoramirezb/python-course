"""
FUNCIÓN: LAMBDA
===============
Funciones anónimas (sin nombre)
"""

print("=" * 50)
print("FUNCIONES LAMBDA")
print("=" * 50)

# Lambda básica
cuadrado = lambda x: x ** 2
print(f"\nLambda básica:")
print(f"  cuadrado = lambda x: x ** 2")
print(f"  cuadrado(5) = {cuadrado(5)}")

# Lambda con múltiples parámetros
sumar = lambda a, b: a + b
print(f"\nLambda con múltiples parámetros:")
print(f"  sumar = lambda a, b: a + b")
print(f"  sumar(3, 4) = {sumar(3, 4)}")

# Lambda con condicional
mayor = lambda x, y: x if x > y else y
print(f"\nLambda con condicional:")
print(f"  mayor = lambda x, y: x if x > y else y")
print(f"  mayor(10, 15) = {mayor(10, 15)}")

# Lambda en funciones de orden superior
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"\nLambda con map():")
print(f"  numeros = {numeros}")
print(f"  map(lambda x: x**2, numeros) = {cuadrados}")

print("\n" + "=" * 50)
