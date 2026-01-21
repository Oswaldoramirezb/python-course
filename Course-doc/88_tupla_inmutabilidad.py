"""
TUPLA: INMUTABILIDAD
====================
Las tuplas NO se pueden modificar
"""

print("=" * 50)
print("INMUTABILIDAD DE TUPLAS")
print("=" * 50)

tupla = (1, 2, 3)
print(f"\nTupla: {tupla}")

print(f"  ✅ Se puede leer: tupla[0] = {tupla[0]}")
print(f"  ✅ Se puede hacer slicing: tupla[1:3] = {tupla[1:3]}")

print(f"\n  ❌ NO se puede modificar:")
print(f"     tupla[0] = 10  # Error: 'tuple' object does not support item assignment")

# Comparar con lista
lista = [1, 2, 3]
lista[0] = 10
print(f"\n  Lista SÍ se puede modificar:")
print(f"     lista[0] = 10 → {lista}")

print("\n" + "=" * 50)
