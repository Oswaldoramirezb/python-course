"""
REGEX: FINDALL
==============
Encontrar todas las coincidencias
"""

print("=" * 50)
print("REGEX FINDALL")
print("=" * 50)

import re

# findall() - encuentra todas las coincidencias
texto = "Los números son 123, 456, 789 y 012"

patron = r"\d+"
resultados = re.findall(patron, texto)

print(f"\nTexto: '{texto}'")
print(f"Patrón: '{patron}' (números)")

print("\nfindall() encuentra todas:")
print(f"  re.findall(patron, texto) = {resultados}")

# Buscar emails
texto2 = "Contactos: juan@email.com, maria@test.com, pedro@example.com"
patron_email = r"\w+@\w+\.\w+"
emails = re.findall(patron_email, texto2)

print(f"\nBuscar todos los emails:")
print(f"  texto = '{texto2}'")
print(f"  emails encontrados: {emails}")

# Buscar palabras
texto3 = "Python es genial, Python es fácil, Python es poderoso"
palabras_python = re.findall(r"Python", texto3)
print(f"\nBuscar 'Python':")
print(f"  texto = '{texto3}'")
print(f"  'Python' aparece {len(palabras_python)} veces: {palabras_python}")

print("\n" + "=" * 50)
