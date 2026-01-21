"""
OPERADOR: ASIGNACIÓN CON MULTIPLICACIÓN (*=)
============================================
Multiplica y asigna el resultado
"""

print("=" * 50)
print("OPERADOR ASIGNACIÓN CON MULTIPLICACIÓN (*=)")
print("=" * 50)

# Asignación con multiplicación
x = 5
print(f"\nValor inicial: x = {x}")

x *= 3  # Equivale a: x = x * 3
print(f"Después de x *= 3:")
print(f"  x ahora es: {x}")

# Ejemplo práctico
numero = 2
print(f"\nEjemplo práctico - Potencias de 2:")
print(f"  numero = {numero}")
numero *= 2
print(f"  numero *= 2 → numero = {numero}")
numero *= 2
print(f"  numero *= 2 → numero = {numero}")

print("\n" + "=" * 50)
