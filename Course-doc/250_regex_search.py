"""
REGEX: SEARCH
=============
Buscar patrón en cualquier parte de la cadena
"""

print("=" * 50)
print("REGEX SEARCH")
print("=" * 50)

import re

# search() - busca en cualquier parte
texto = "Mi email es usuario@email.com y mi teléfono es 123-456-7890"

print(f"\nTexto: '{texto}'")

# Buscar email
patron_email = r"\w+@\w+\.\w+"
resultado_email = re.search(patron_email, texto)
print("\nBuscar email:")
if resultado_email:
    print(f"  Encontrado: {resultado_email.group()}")
    print(f"  Posición: {resultado_email.start()}-{resultado_email.end()}")

# Buscar teléfono
patron_telefono = r"\d{3}-\d{3}-\d{4}"
resultado_telefono = re.search(patron_telefono, texto)
print("\nBuscar teléfono:")
if resultado_telefono:
    print(f"  Encontrado: {resultado_telefono.group()}")

# Comparación: match vs search
print("\nComparación:")
print("  match() - Solo al inicio")
print("  search() - En cualquier parte")

texto_test = "Python es genial"
print(f"\n  texto = '{texto_test}'")
print(f"  re.match('Python', texto) = {bool(re.match('Python', texto))}")
print(f"  re.search('Python', texto) = {bool(re.search('Python', texto))}")

print("\n" + "=" * 50)
