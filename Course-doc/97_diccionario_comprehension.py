"""
DICCIONARIO: COMPREHENSION
==========================
Crear diccionarios de forma concisa
"""

print("=" * 50)
print("DICT COMPREHENSION")
print("=" * 50)

# Comprehension básica
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"\nCuadrados: {cuadrados}")
print(f"  {{x: x**2 for x in range(1, 6)}}")

# Comprehension con condición
pares = {x: x*2 for x in range(1, 6) if x % 2 == 0}
print(f"\nPares: {pares}")

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
print(f"\nInvertir:")
print(f"  Original: {original}")
print(f"  Invertido: {invertido}")

# Desde lista
palabras = ["uno", "dos", "tres"]
longitudes = {palabra: len(palabra) for palabra in palabras}
print(f"\nLongitudes: {longitudes}")

print("\n" + "=" * 50)
