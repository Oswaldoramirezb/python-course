"""
INPUT: CON NÚMEROS
==================
Pedir números al usuario (importante: convertir)
"""

print("=" * 50)
print("INPUT CON NÚMEROS")
print("=" * 50)

# ⚠️ IMPORTANTE: input() siempre retorna texto
print("\n⚠️  IMPORTANTE:")
print("  input() SIEMPRE retorna texto (str)")
print("  Debes convertir a int o float")

# Ejemplo con int
print("\nEjemplo 1 - Convertir a entero:")
print("  edad = int(input('Ingresa tu edad: '))")
edad_texto = "25"  # Simulación
edad = int(edad_texto)
print(f"  Si el usuario escribe '25':")
print(f"  edad = {edad} (tipo: {type(edad).__name__})")

# Ejemplo con float
print("\nEjemplo 2 - Convertir a decimal:")
print("  precio = float(input('Ingresa el precio: '))")
precio_texto = "19.99"  # Simulación
precio = float(precio_texto)
print(f"  Si el usuario escribe '19.99':")
print(f"  precio = {precio} (tipo: {type(precio).__name__})")

# Manejo de errores
print("\nEjemplo 3 - Manejo de errores:")
print("  try:")
print("      numero = int(input('Ingresa un número: '))")
print("  except ValueError:")
print("      print('Error: Debes ingresar un número válido')")

print("\n" + "=" * 50)
