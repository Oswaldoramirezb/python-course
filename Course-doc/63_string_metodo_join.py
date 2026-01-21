"""
STRING: MÉTODO JOIN
====================
Une elementos de una lista en una cadena
"""

print("=" * 50)
print("MÉTODO JOIN()")
print("=" * 50)

# join() - unir lista en cadena
palabras = ["Python", "es", "genial"]
print(f"\nLista: {palabras}")

texto = " ".join(palabras)
print(f"Después de ' '.join(): '{texto}'")

# join() con separador diferente
print(f"\nCon separador '-'")
texto2 = "-".join(palabras)
print(f"  '-'.join({palabras}) = '{texto2}'")

# join() con números (convertir primero)
numeros = [1, 2, 3]
print(f"\nCon números (convertir a str primero):")
print(f"  numeros = {numeros}")
texto3 = ", ".join(str(n) for n in numeros)
print(f"  ', '.join(str(n) for n in numeros) = '{texto3}'")

print("\n" + "=" * 50)
