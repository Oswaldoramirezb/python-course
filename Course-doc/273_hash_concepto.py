"""
HASH: CONCEPTO
==============
¿Qué es un hash?
"""

print("=" * 50)
print("CONCEPTO DE HASH")
print("=" * 50)

print("\nHash:")
print("  - Valor numérico único para un objeto")
print("  - Identificador rápido")
print("  - Usado en diccionarios y sets")

print("\nCaracterísticas:")
print("  - Mismo objeto → mismo hash")
print("  - Objetos iguales → mismo hash")
print("  - Hash inmutable durante vida del objeto")

print("\nEjemplo:")
print("  hash('Python') = valor numérico")
print("  hash(123) = valor numérico")

texto = "Python"
valor_hash = hash(texto)
print(f"\nEjemplo práctico:")
print(f"  texto = '{texto}'")
print(f"  hash(texto) = {valor_hash}")

print("\nUsos:")
print("  ✅ Claves en diccionarios")
print("  ✅ Elementos en sets")
print("  ✅ Búsqueda rápida (O(1))")

print("\nHashables:")
print("  - Objetos que tienen hash")
print("  - Pueden ser claves en dict o elementos en set")
print("  - Deben ser inmutables")

print("\n" + "=" * 50)
