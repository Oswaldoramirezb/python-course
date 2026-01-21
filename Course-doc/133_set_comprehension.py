"""
COMPREHENSION: SET COMPREHENSION
================================
Crear sets de forma concisa
"""

print("=" * 50)
print("SET COMPREHENSION")
print("=" * 50)

# Comprehension básica
cuadrados = {x**2 for x in range(1, 6)}
print(f"\nCuadrados: {cuadrados}")
print(f"  {{x**2 for x in range(1, 6)}}")

# Comprehension con condición
pares = {x for x in range(10) if x % 2 == 0}
print(f"\nCon condición (pares):")
print(f"  {{x for x in range(10) if x % 2 == 0}} = {pares}")

# Desde cadena (caracteres únicos)
texto = "programación"
caracteres_unicos = {c for c in texto}
print(f"\nCaracteres únicos:")
print(f"  texto = '{texto}'")
print(f"  caracteres_unicos = {caracteres_unicos}")

# Longitudes de palabras
palabras = ["hola", "mundo", "python", "hola"]
longitudes = {len(palabra) for palabra in palabras}
print(f"\nLongitudes únicas:")
print(f"  palabras = {palabras}")
print(f"  longitudes = {longitudes}")

print("\n" + "=" * 50)
