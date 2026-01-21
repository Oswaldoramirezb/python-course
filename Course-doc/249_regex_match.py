"""
REGEX: MATCH
============
Buscar patrón al inicio de una cadena
"""

print("=" * 50)
print("REGEX MATCH")
print("=" * 50)

import re

# match() - busca al inicio
texto1 = "Python es genial"
texto2 = "Amo Python"

patron = r"Python"

print("\nmatch() busca al INICIO:")
print(f"  texto1 = '{texto1}'")
print(f"  texto2 = '{texto2}'")
print(f"  patron = '{patron}'")

resultado1 = re.match(patron, texto1)
resultado2 = re.match(patron, texto2)

print(f"\n  re.match(patron, texto1) = {resultado1}")
if resultado1:
    print(f"    Encontrado: {resultado1.group()}")

print(f"\n  re.match(patron, texto2) = {resultado2}")
if resultado2:
    print(f"    Encontrado: {resultado2.group()}")
else:
    print(f"    No encontrado (no está al inicio)")

# Ejemplo práctico
print("\nEjemplo práctico - Validar que empiece con número:")
texto3 = "123abc"
texto4 = "abc123"

patron_numero = r"^\d"
print(f"  '{texto3}' empieza con número: {bool(re.match(patron_numero, texto3))}")
print(f"  '{texto4}' empieza con número: {bool(re.match(patron_numero, texto4))}")

print("\n" + "=" * 50)
