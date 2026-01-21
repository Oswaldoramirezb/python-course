"""
ALGORITMOS: ORDENAMIENTO RÁPIDO
================================
Quicksort - Ordenamiento eficiente
"""

print("=" * 50)
print("ORDENAMIENTO RÁPIDO (QUICKSORT)")
print("=" * 50)

def quicksort(lista):
    """Quicksort - O(n log n) promedio"""
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    return quicksort(menores) + iguales + quicksort(mayores)

lista = [64, 34, 25, 12, 22, 11, 90]
print(f"\nLista original: {lista}")

lista_ordenada = quicksort(lista)
print(f"Lista ordenada: {lista_ordenada}")

print("\nAlgoritmo:")
print("  1. Elegir pivote")
print("  2. Dividir en menores, iguales, mayores")
print("  3. Ordenar recursivamente menores y mayores")
print("  4. Combinar: menores + iguales + mayores")

print("\nComplejidad:")
print("  Tiempo promedio: O(n log n)")
print("  Tiempo peor caso: O(n²)")
print("  Espacio: O(log n)")

print("\nVentajas:")
print("  ✅ Rápido en promedio")
print("  ✅ O(n log n) típicamente")
print("  ✅ Eficiente en la práctica")

print("\nDesventajas:")
print("  ❌ O(n²) en peor caso")
print("  ❌ No estable")
print("  ❌ Requiere espacio adicional")

print("\nCuándo usar:")
print("  - Listas grandes")
print("  - Cuando la velocidad importa")
print("  - Ordenamiento general")

print("\n" + "=" * 50)
