"""
RESUMEN: HASH Y HASHABLES
=========================
Todas las operaciones con hash
"""

print("=" * 50)
print("RESUMEN - HASH Y HASHABLES")
print("=" * 50)

print("\nHash:")
print("  - Valor numérico único para un objeto")
print("  - Usado en diccionarios y sets")
print("  - hash(objeto) → valor numérico")

print("\nHashables:")
print("  - Objetos que tienen hash")
print("  - Pueden ser claves en dict o elementos en set")
print("  - Deben ser inmutables")

print("\nTipos hashables:")
print("  ✅ int, float, str, bool")
print("  ✅ tuple (si elementos hashables)")
print("  ✅ frozenset")
print("  ❌ list, dict, set (mutables)")

print("\nUsar hash():")
print("  hash(objeto) → valor numérico")
print("  Mismo objeto → mismo hash")
print("  Objetos iguales → mismo hash")

print("\nEn diccionarios y sets:")
print("  dict[clave_hashable] = valor")
print("  set(elemento_hashable)")

print("\nObjetos personalizados:")
print("  - Implementar __hash__() y __eq__()")
print("  - Objeto debe ser inmutable")
print("  - Hash consistente con igualdad")

print("\nVentajas:")
print("  ✅ Búsqueda rápida O(1)")
print("  ✅ Eficiencia en dict y set")
print("  ✅ Identificación rápida")

print("\n" + "=" * 50)
