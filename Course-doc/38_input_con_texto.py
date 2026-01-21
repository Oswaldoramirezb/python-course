"""
INPUT: CON TEXTO
================
Pedir texto al usuario
"""

print("=" * 50)
print("INPUT CON TEXTO")
print("=" * 50)

# Input básico (simulado)
print("\nEjemplo 1 - Pedir nombre:")
print("  nombre = input('Ingresa tu nombre: ')")
print("  Si el usuario escribe 'Ana', entonces:")
nombre = "Ana"  # Simulación
print(f"  nombre = '{nombre}'")
print(f"  print(f'Hola, {nombre}!')")
print(f"  Resultado: Hola, {nombre}!")

# Input con validación
print("\nEjemplo 2 - Validar que no esté vacío:")
print("  ciudad = input('Ingresa tu ciudad: ')")
ciudad = "Madrid"  # Simulación
if ciudad:
    print(f"  ✅ Ciudad ingresada: {ciudad}")
else:
    print("  ❌ No ingresaste ninguna ciudad")

print("\n" + "=" * 50)
