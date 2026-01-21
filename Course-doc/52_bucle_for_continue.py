"""
BUCLE FOR: CONTINUE
===================
Saltar a la siguiente iteración sin terminar la actual
"""

print("=" * 50)
print("BUCLE FOR CON CONTINUE")
print("=" * 50)

# Continue básico - saltar números pares
print("\nEjemplo 1 - Solo números impares:")
for i in range(10):
    if i % 2 == 0:
        continue  # Saltar números pares
    print(f"  Número impar: {i}")

# Continue - procesar solo elementos válidos
print("\nEjemplo 2 - Procesar solo positivos:")
numeros = [5, -3, 10, -1, 8, 0]
print(f"  Lista: {numeros}")
for num in numeros:
    if num <= 0:
        continue  # Saltar negativos y cero
    print(f"  Número positivo: {num}")

print("\n" + "=" * 50)
