"""
INPUT - ENTRADA DE DATOS
========================
Permite al usuario ingresar datos desde el teclado
"""

print("=" * 50)
print("INPUT - Entrada de Datos")
print("=" * 50)

# Input básico (comentado para que no pida entrada real)
# nombre = input("Ingresa tu nombre: ")
# print(f"Hola, {nombre}!")

# Simulamos el input
print("\nEjemplo 1: Pedir nombre")
print("  nombre = input('Ingresa tu nombre: ')")
print("  Si el usuario escribe 'Juan', entonces:")
nombre = "Juan"  # Simulación
print(f"  nombre = '{nombre}'")
print(f"  print(f'Hola, {nombre}!')")
print(f"  Resultado: Hola, {nombre}!")

print("\nEjemplo 2: Pedir número")
print("  edad = input('Ingresa tu edad: ')")
print("  ⚠️  IMPORTANTE: input() siempre retorna texto (str)")
edad_texto = "25"  # Simulación
print(f"  edad = '{edad_texto}' (es texto, no número)")
print(f"  tipo: {type(edad_texto).__name__}")

print("\nPara convertir a número:")
print("  edad = int(input('Ingresa tu edad: '))")
edad_numero = int(edad_texto)
print(f"  edad = {edad_numero} (ahora es número)")
print(f"  tipo: {type(edad_numero).__name__}")

print("\n" + "=" * 50)
