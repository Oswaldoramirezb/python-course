"""
OUTPUT: PRINT CON SEP Y END
===========================
Controlar separadores y final de línea
"""

print("=" * 50)
print("PRINT CON SEP Y END")
print("=" * 50)

# sep: separador entre elementos
print("\nCon sep (separador):")
print("Python", "es", "genial", sep=" - ")

# end: qué poner al final (por defecto es \n)
print("\nCon end (final de línea):")
print("Hola", end=" ")
print("Mundo", end="!")
print()  # Nueva línea

# Combinar sep y end
print("\nCombinando sep y end:")
print("1", "2", "3", sep=", ", end=" → ")
print("Listo!")

print("\n" + "=" * 50)
