"""
ALGORITMOS: BÚSQUEDA LINEAL
===========================
Buscar elemento en lista
"""

print("=" * 50)
print("BÚSQUEDA LINEAL")
print("=" * 50)

def busqueda_lineal(lista, objetivo):
    """Búsqueda lineal - O(n)"""
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1

lista = [3, 1, 4, 1, 5, 9, 2, 6]
objetivo = 5

print(f"\nLista: {lista}")
print(f"Buscar: {objetivo}")

resultado = busqueda_lineal(lista, objetivo)
print(f"\nResultado:")
if resultado != -1:
    print(f"  Encontrado en índice {resultado}")
else:
    print(f"  No encontrado")

print("\nAlgoritmo:")
print("  def busqueda_lineal(lista, objetivo):")
print("      for i, elemento in enumerate(lista):")
print("          if elemento == objetivo:")
print("              return i")
print("      return -1")

print("\nComplejidad:")
print("  Tiempo: O(n) - Lineal")
print("  Espacio: O(1) - Constante")

print("\nVentajas:")
print("  ✅ Simple")
print("  ✅ Funciona con listas no ordenadas")
print("  ✅ No requiere ordenamiento previo")

print("\nDesventajas:")
print("  ❌ Lento para listas grandes")
print("  ❌ O(n) en el peor caso")

print("\nCuándo usar:")
print("  - Listas pequeñas")
print("  - Listas no ordenadas")
print("  - Búsqueda única")

print("\n" + "=" * 50)
