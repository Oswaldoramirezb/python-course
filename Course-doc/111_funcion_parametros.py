"""
FUNCIÓN: PARÁMETROS
===================
Pasar información a una función
"""

print("=" * 50)
print("PARÁMETROS DE FUNCIONES")
print("=" * 50)

# Función con un parámetro
def saludar(nombre):
    return f"Hola, {nombre}!"

print("\nUn parámetro:")
print(f"  saludar('Juan') = {saludar('Juan')}")

# Función con múltiples parámetros
def sumar(a, b):
    return a + b

print(f"\nMúltiples parámetros:")
print(f"  sumar(5, 3) = {sumar(5, 3)}")

# Función con 3 parámetros
def calcular_promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(f"\nTres parámetros:")
print(f"  calcular_promedio(10, 20, 30) = {calcular_promedio(10, 20, 30)}")

print("\n" + "=" * 50)
