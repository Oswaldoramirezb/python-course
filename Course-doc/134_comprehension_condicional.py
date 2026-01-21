"""
COMPREHENSION: CON CONDICIONALES
=================================
Usar if-else en comprehensions
"""

print("=" * 50)
print("COMPREHENSIONS CON CONDICIONALES")
print("=" * 50)

# if en comprehension (filtro)
pares = [x for x in range(10) if x % 2 == 0]
print(f"\nif como filtro:")
print(f"  [x for x in range(10) if x % 2 == 0] = {pares}")

# if-else en comprehension (transformación)
resultado = [x if x % 2 == 0 else -x for x in range(10)]
print(f"\nif-else como transformación:")
print(f"  [x if x % 2 == 0 else -x for x in range(10)] = {resultado}")

# Múltiples condiciones
resultado2 = [x for x in range(20) if x % 2 == 0 if x > 10]
print(f"\nMúltiples condiciones:")
print(f"  [x for x in range(20) if x % 2 == 0 if x > 10] = {resultado2}")

# Con diccionario
clasificacion = {x: "par" if x % 2 == 0 else "impar" for x in range(5)}
print(f"\nCon diccionario:")
print(f"  {{x: 'par' if x%2==0 else 'impar' for x in range(5)}} = {clasificacion}")

print("\n" + "=" * 50)
