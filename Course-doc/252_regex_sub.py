"""
REGEX: SUB
==========
Reemplazar texto usando patrones
"""

print("=" * 50)
print("REGEX SUB (REEMPLAZAR)")
print("=" * 50)

import re

# sub() - reemplazar
texto = "Mi teléfono es 123-456-7890"

print(f"\nTexto original: '{texto}'")

# Reemplazar guiones
texto_nuevo = re.sub(r"-", "", texto)
print(f"\nReemplazar guiones:")
print(f"  re.sub(r'-', '', texto) = '{texto_nuevo}'")

# Enmascarar números
texto_enmascarado = re.sub(r"\d", "X", texto)
print(f"\nEnmascarar dígitos:")
print(f"  re.sub(r'\\d', 'X', texto) = '{texto_enmascarado}'")

# Reemplazar con función
def enmascarar_email(match):
    email = match.group()
    partes = email.split("@")
    return f"{partes[0][0]}***@{partes[1]}"

texto2 = "Contacto: juan@email.com"
texto_enmascarado2 = re.sub(r"\w+@\w+\.\w+", enmascarar_email, texto2)
print(f"\nReemplazar con función:")
print(f"  texto = '{texto2}'")
print(f"  resultado = '{texto_enmascarado2}'")

# Contar reemplazos
texto3 = "Python Python Python"
nuevo, contador = re.subn(r"Python", "Java", texto3)
print(f"\nContar reemplazos:")
print(f"  re.subn(r'Python', 'Java', texto) = ('{nuevo}', {contador})")

print("\n" + "=" * 50)
