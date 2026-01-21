"""
HASHABLES: EN DICT Y SET
========================
Usar objetos hashables como claves
"""

print("=" * 50)
print("HASHABLES EN DICT Y SET")
print("=" * 50)

# Diccionario con claves hashables
diccionario = {
    123: "número",
    "texto": "cadena",
    (1, 2): "tupla",
    True: "booleano"
}

print("\nDiccionario con claves hashables:")
print(f"  {diccionario}")

# Acceder
print(f"\nAcceder:")
print(f"  diccionario[123] = {diccionario[123]}")
print(f"  diccionario[(1, 2)] = {diccionario[(1, 2)]}")

# Set con elementos hashables
conjunto = {1, 2, 3, "texto", (4, 5)}
print(f"\nSet con elementos hashables:")
print(f"  {conjunto}")

# Error: intentar usar lista como clave
print("\n⚠️  Error - Lista no es hashable:")
try:
    diccionario_error = {[1, 2]: "error"}
except TypeError as e:
    print(f"  TypeError: {e}")

# Solución: usar tupla
print("\nSolución - Usar tupla:")
diccionario_ok = {tuple([1, 2]): "OK"}
print(f"  {diccionario_ok}")

print("\n" + "=" * 50)
