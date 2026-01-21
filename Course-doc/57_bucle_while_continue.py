"""
BUCLE WHILE: CONTINUE
=====================
Saltar a la siguiente iteración
"""

print("=" * 50)
print("BUCLE WHILE CON CONTINUE")
print("=" * 50)

# While con continue
print("\nEjemplo 1 - Solo números impares:")
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue  # Saltar números pares
    print(f"  Número impar: {numero}")

# Validación con continue
print("\nEjemplo 2 - Validar entrada (simulado):")
intentos = 0
while intentos < 3:
    intentos += 1
    entrada = "válida" if intentos == 2 else "inválida"  # Simulación
    if entrada == "inválida":
        print(f"  Intento {intentos}: Entrada inválida, reintentando...")
        continue
    print(f"  ✅ Intento {intentos}: Entrada válida!")
    break

print("\n" + "=" * 50)
