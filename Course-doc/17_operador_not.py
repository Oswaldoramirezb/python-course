"""
OPERADOR: NOT
=============
Invierte el valor: True se vuelve False, False se vuelve True
"""

print("=" * 50)
print("OPERADOR NOT")
print("=" * 50)

# NOT con True
resultado1 = not True
print(f"\nnot True = {resultado1}")

# NOT con False
resultado2 = not False
print(f"not False = {resultado2}")

# Ejemplo práctico
es_fin_de_semana = False
trabaja = not es_fin_de_semana

print(f"\nEjemplo práctico:")
print(f"  es_fin_de_semana = {es_fin_de_semana}")
print(f"  trabaja = not es_fin_de_semana")
print(f"  Resultado: {trabaja}")

print("\n" + "=" * 50)
