"""
LISTA: COMPREHENSION
====================
Crear listas de forma concisa
"""

print("=" * 50)
print("LIST COMPREHENSION")
print("=" * 50)

# Comprehension básica
cuadrados = [x**2 for x in range(1, 6)]
print(f"\nCuadrados: {cuadrados}")
print(f"  [x**2 for x in range(1, 6)]")

# Comprehension con condición
pares = [x for x in range(10) if x % 2 == 0]
print(f"\nNúmeros pares: {pares}")
print(f"  [x for x in range(10) if x % 2 == 0]")

# Comprehension con múltiples condiciones
resultado = [x for x in range(20) if x % 2 == 0 if x > 10]
print(f"\nPares mayores que 10: {resultado}")

# Comparación: for vs comprehension
print(f"\nComparación:")
print(f"  Con for: {[x*2 for x in range(5)]}")
print(f"  Con comprehension: {[x*2 for x in range(5)]}")

print("\n" + "=" * 50)
