"""
LISTA: ANIDADAS
===============
Listas dentro de listas
"""

print("=" * 50)
print("LISTAS ANIDADAS")
print("=" * 50)

# Lista anidada (matriz)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMatriz: {matriz}")

# Acceder a elementos
print(f"  matriz[0] = {matriz[0]} (primera fila)")
print(f"  matriz[1][2] = {matriz[1][2]} (fila 1, columna 2)")

# Iterar sobre lista anidada
print(f"\nIterar sobre matriz:")
for i, fila in enumerate(matriz):
    print(f"  Fila {i}: {fila}")

# Crear matriz
matriz2 = [[0 for j in range(3)] for i in range(3)]
print(f"\nMatriz 3x3 de ceros: {matriz2}")

print("\n" + "=" * 50)
