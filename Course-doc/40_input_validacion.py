"""
INPUT: VALIDACIÓN
=================
Validar que la entrada del usuario sea correcta
"""

print("=" * 50)
print("INPUT CON VALIDACIÓN")
print("=" * 50)

# Validación con bucle
print("\nEjemplo - Validar edad (simulado):")
print("  while True:")
print("      try:")
print("          edad = int(input('Ingresa tu edad: '))")
print("          if edad > 0 and edad < 120:")
print("              break")
print("          else:")
print("              print('Edad inválida')")
print("      except ValueError:")
print("          print('Debes ingresar un número')")

# Simulación del proceso
edad_valida = 25  # Simulación
print(f"\n  ✅ Edad válida ingresada: {edad_valida}")

# Validación de texto
print("\nEjemplo - Validar email (simulado):")
email = "usuario@email.com"  # Simulación
if '@' in email and '.' in email.split('@')[1]:
    print(f"  ✅ Email válido: {email}")
else:
    print(f"  ❌ Email inválido: {email}")

print("\n" + "=" * 50)
