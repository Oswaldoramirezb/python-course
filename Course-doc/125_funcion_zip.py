"""
FUNCIÓN: ZIP
============
Combinar múltiples secuencias
"""

print("=" * 50)
print("FUNCIÓN ZIP()")
print("=" * 50)

# zip() básico
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
print(f"\nListas:")
print(f"  nombres = {nombres}")
print(f"  edades = {edades}")

# Combinar con zip
combinado = list(zip(nombres, edades))
print(f"\nzip(nombres, edades) = {combinado}")

# Iterar sobre zip
print(f"\nIterar sobre zip:")
for nombre, edad in zip(nombres, edades):
    print(f"  {nombre} tiene {edad} años")

# Tres listas
ciudades = ["Barcelona", "Madrid", "Valencia"]
print(f"\nTres listas:")
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"  {nombre}, {edad} años, de {ciudad}")

# Desempaquetar
nombres2, edades2 = zip(*combinado)
print(f"\nDesempaquetar:")
print(f"  nombres2 = {nombres2}")
print(f"  edades2 = {edades2}")

print("\n" + "=" * 50)
