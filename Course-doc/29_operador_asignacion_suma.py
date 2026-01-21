"""
OPERADOR: ASIGNACIÓN CON SUMA (+=)
===================================
Suma y asigna el resultado
"""

print("=" * 50)
print("OPERADOR ASIGNACIÓN CON SUMA (+=)")
print("=" * 50)

# Asignación con suma
x = 10
print(f"\nValor inicial: x = {x}")

x += 5  # Equivale a: x = x + 5
print(f"Después de x += 5:")
print(f"  x ahora es: {x}")

# Ejemplo práctico
contador = 0
print(f"\nEjemplo práctico - Contador:")
print(f"  contador = {contador}")
contador += 1
print(f"  contador += 1 → contador = {contador}")
contador += 1
print(f"  contador += 1 → contador = {contador}")

print("\n" + "=" * 50)
