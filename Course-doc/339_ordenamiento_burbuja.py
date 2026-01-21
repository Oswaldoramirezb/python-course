"""
ALGORITMOS: ORDENAMIENTO BURBUJA
=================================
Ordenar lista con bubble sort
"""

print("=" * 50)
print("ORDENAMIENTO BURBUJA")
print("=" * 50)

def ordenamiento_burbuja(lista):
    """Bubble sort - O(n²)"""
    n = len(lista)
    lista_copia = lista.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia

lista = [64, 34, 25, 12, 22, 11, 90]
print(f"\nLista original: {lista}")

lista_ordenada = ordenamiento_burbuja(lista)
print(f"Lista ordenada: {lista_ordenada}")

print("\nAlgoritmo:")
print("  1. Comparar elementos adyacentes")
print("  2. Si están en orden incorrecto, intercambiar")
print("  3. Repetir para todos los elementos")
print("  4. Repetir hasta que no haya intercambios")

print("\nComplejidad:")
print("  Tiempo: O(n²) - Cuadrática")
print("  Espacio: O(1) - Constante")

print("\nVentajas:")
print("  ✅ Simple de entender")
print("  ✅ Fácil de implementar")
print("  ✅ Estable (mantiene orden relativo)")

print("\nDesventajas:")
print("  ❌ Muy lento O(n²)")
print("  ❌ No eficiente para listas grandes")

print("\nCuándo usar:")
print("  - Listas pequeñas")
print("  - Propósitos educativos")
print("  - Cuando la simplicidad importa más que velocidad")

print("\n" + "=" * 50)
