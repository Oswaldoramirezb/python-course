"""
COLLECTIONS: CHAINMAP
=====================
Combinar múltiples diccionarios
"""

print("=" * 50)
print("CHAINMAP")
print("=" * 50)

from collections import ChainMap

# Crear ChainMap
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 5, "e": 6}

chain = ChainMap(dict1, dict2, dict3)

print("\nChainMap combina diccionarios:")
print(f"  dict1 = {dict1}")
print(f"  dict2 = {dict2}")
print(f"  dict3 = {dict3}")

print(f"\nChainMap(dict1, dict2, dict3):")
print(f"  chain = {dict(chain)}")

# Acceder a valores
print(f"\nAcceder:")
print(f"  chain['a'] = {chain['a']} (de dict1)")
print(f"  chain['b'] = {chain['b']} (de dict1, primero encontrado)")
print(f"  chain['c'] = {chain['c']} (de dict2)")

# Modificar afecta al primer diccionario
chain["nuevo"] = 10
print(f"\nModificar:")
print(f"  chain['nuevo'] = 10")
print(f"  dict1 = {dict1} (modificado)")

print("\nUso:")
print("  ✅ Combinar configuraciones")
print("  ✅ Búsqueda en múltiples diccionarios")
print("  ✅ Jerarquía de valores")

print("\n" + "=" * 50)
