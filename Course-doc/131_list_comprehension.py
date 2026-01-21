"""
COMPREHENSION: LIST COMPREHENSION
=================================
Crear listas de forma concisa
"""

print("=" * 50)
print("LIST COMPREHENSION")
print("=" * 50)

# Comprehension básica
cuadrados = [x**2 for x in range(1, 6)]
print(f"\nCuadrados: {cuadrados}")
print(f"  [x**2 for x in range(1, 6)]")

# Comparación: for vs comprehension
print(f"\nComparación:")
print(f"  Con for:")
cuadrados_for = []
for x in range(1, 6):
    cuadrados_for.append(x**2)
print(f"    {cuadrados_for}")

print(f"  Con comprehension: {cuadrados}")

# Comprehension con condición
pares = [x for x in range(10) if x % 2 == 0]
print(f"\nCon condición (pares):")
print(f"  [x for x in range(10) if x % 2 == 0] = {pares}")

# Múltiples condiciones
resultado = [x for x in range(20) if x % 2 == 0 if x > 10]
print(f"\nMúltiples condiciones:")
print(f"  [x for x in range(20) if x % 2 == 0 if x > 10] = {resultado}")

print("\n" + "=" * 50)
