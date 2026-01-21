"""
OPERADOR: OR
============
Si AL MENOS UNA condición es True, el resultado es True
"""

print("=" * 50)
print("OPERADOR OR")
print("=" * 50)

# OR con True y False
resultado1 = True or False
print(f"\nTrue or False = {resultado1}")

# OR con False y False
resultado2 = False or False
print(f"False or False = {resultado2}")

# Ejemplo práctico
es_estudiante = False
es_senior = True

tiene_descuento = es_estudiante or es_senior

print(f"\nEjemplo práctico:")
print(f"  es_estudiante = {es_estudiante}")
print(f"  es_senior = {es_senior}")
print(f"  tiene_descuento = es_estudiante or es_senior")
print(f"  Resultado: {tiene_descuento}")

print("\n" + "=" * 50)
