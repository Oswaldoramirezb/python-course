"""
BUCLE FOR: ANIDADOS
===================
Bucles dentro de otros bucles
"""

print("=" * 50)
print("BUCLE FOR ANIDADOS")
print("=" * 50)

# Tabla de multiplicar
print("\nEjemplo 1 - Tabla de multiplicar:")
for i in range(1, 4):
    for j in range(1, 4):
        resultado = i * j
        print(f"  {i} x {j} = {resultado}")

# Matriz
print("\nEjemplo 2 - Iterar sobre matriz:")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(f"  {elemento}", end=" ")
    print()  # Nueva línea

# Combinaciones
print("\nEjemplo 3 - Combinaciones:")
colores = ["rojo", "azul"]
tallas = ["S", "M"]
for color in colores:
    for talla in tallas:
        print(f"  {color} talla {talla}")

print("\n" + "=" * 50)
