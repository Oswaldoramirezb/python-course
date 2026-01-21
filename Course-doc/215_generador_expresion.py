"""
GENERADOR: EXPRESIÓN
====================
Generadores con sintaxis de comprensión
"""

print("=" * 50)
print("GENERADOR EXPRESIÓN")
print("=" * 50)

# Generador expresión (similar a list comprehension)
cuadrados = (x**2 for x in range(1, 6))
print("\nGenerador expresión:")
print("  cuadrados = (x**2 for x in range(1, 6))")
print("  (usa paréntesis en lugar de corchetes)")

print("\nIterar sobre generador:")
for cuadrado in cuadrados:
    print(f"  {cuadrado}")

# Comparación: lista vs generador
print("\nComparación:")
lista = [x**2 for x in range(1, 6)]
generador = (x**2 for x in range(1, 6))

print(f"  Lista: {lista} (todos los valores en memoria)")
print(f"  Generador: {generador} (objeto generador)")

# Generador con condición
pares = (x for x in range(10) if x % 2 == 0)
print("\nGenerador con condición:")
print("  pares = (x for x in range(10) if x % 2 == 0)")
print("  Valores:", list(pares))

print("\nVentajas:")
print("  ✅ Menor uso de memoria")
print("  ✅ Sintaxis concisa")
print("  ✅ Eficiente para secuencias grandes")

print("\n" + "=" * 50)
