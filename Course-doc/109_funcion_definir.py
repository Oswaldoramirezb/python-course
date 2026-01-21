"""
FUNCIÓN: DEFINIR
================
Crear una función en Python
"""

print("=" * 50)
print("DEFINIR FUNCIONES")
print("=" * 50)

# Definir función básica
def saludar():
    """Función que imprime un saludo"""
    print("  ¡Hola, mundo!")

print("\nFunción definida:")
print("  def saludar():")
print("      print('¡Hola, mundo!')")

print("\nLlamar la función:")
saludar()

# Función con parámetros
def saludar_persona(nombre):
    """Saluda a una persona específica"""
    print(f"  ¡Hola, {nombre}!")

print("\nFunción con parámetro:")
print("  def saludar_persona(nombre):")
print("      print(f'¡Hola, {nombre}!')")
saludar_persona("Juan")

print("\n" + "=" * 50)
