"""
BUCLE FOR: CON LISTAS
=====================
Iterar sobre elementos de una lista
"""

print("=" * 50)
print("BUCLE FOR CON LISTAS")
print("=" * 50)

# Iterar sobre lista
print("\nEjemplo 1 - Lista simple:")
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(f"  Número: {numero}")

# Iterar con índice
print("\nEjemplo 2 - Con enumerate (índice y valor):")
frutas = ["manzana", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"  Índice {indice}: {fruta}")

# Modificar lista mientras iteras
print("\nEjemplo 3 - Duplicar valores:")
numeros = [1, 2, 3]
print(f"  Lista original: {numeros}")
for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2
print(f"  Lista modificada: {numeros}")

print("\n" + "=" * 50)
