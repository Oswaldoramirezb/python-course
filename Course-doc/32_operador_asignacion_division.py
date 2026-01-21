"""
OPERADOR: ASIGNACIÓN CON DIVISIÓN (/=)
=======================================
Divide y asigna el resultado
"""

print("=" * 50)
print("OPERADOR ASIGNACIÓN CON DIVISIÓN (/=)")
print("=" * 50)

# Asignación con división
x = 20
print(f"\nValor inicial: x = {x}")

x /= 4  # Equivale a: x = x / 4
print(f"Después de x /= 4:")
print(f"  x ahora es: {x}")

# Ejemplo práctico
precio = 100
print(f"\nEjemplo práctico - Descuento:")
print(f"  precio = ${precio}")
precio /= 2  # 50% de descuento
print(f"  precio /= 2 (50% descuento) → precio = ${precio}")

print("\n" + "=" * 50)
