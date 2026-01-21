"""
OPERADOR: ASIGNACIÓN CON RESTA (-=)
====================================
Resta y asigna el resultado
"""

print("=" * 50)
print("OPERADOR ASIGNACIÓN CON RESTA (-=)")
print("=" * 50)

# Asignación con resta
x = 20
print(f"\nValor inicial: x = {x}")

x -= 5  # Equivale a: x = x - 5
print(f"Después de x -= 5:")
print(f"  x ahora es: {x}")

# Ejemplo práctico
saldo = 100
print(f"\nEjemplo práctico - Saldo:")
print(f"  saldo = ${saldo}")
saldo -= 25
print(f"  saldo -= 25 → saldo = ${saldo}")
saldo -= 15
print(f"  saldo -= 15 → saldo = ${saldo}")

print("\n" + "=" * 50)
