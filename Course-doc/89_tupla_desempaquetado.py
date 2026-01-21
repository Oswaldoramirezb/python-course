"""
TUPLA: DESEMPAQUETADO
=====================
Asignar elementos de tupla a variables
"""

print("=" * 50)
print("DESEMPAQUETADO DE TUPLAS")
print("=" * 50)

# Desempaquetado básico
coordenadas = (3, 4)
x, y = coordenadas
print(f"\nTupla: {coordenadas}")
print(f"  x, y = coordenadas")
print(f"  x = {x}, y = {y}")

# Múltiples valores
datos = ("Juan", 30, "Madrid")
nombre, edad, ciudad = datos
print(f"\nMúltiples valores:")
print(f"  datos = {datos}")
print(f"  nombre, edad, ciudad = datos")
print(f"  nombre = {nombre}, edad = {edad}, ciudad = {ciudad}")

# Intercambiar variables
a = 5
b = 10
print(f"\nIntercambiar variables:")
print(f"  Antes: a={a}, b={b}")
a, b = b, a
print(f"  Después: a={a}, b={b}")

print("\n" + "=" * 50)
