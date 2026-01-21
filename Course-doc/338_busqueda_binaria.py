"""
ALGORITMOS: BÚSQUEDA BINARIA
============================
Buscar en lista ordenada
"""

print("=" * 50)
print("BÚSQUEDA BINARIA")
print("=" * 50)

def busqueda_binaria(lista, objetivo):
    """Búsqueda binaria - O(log n)"""
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1

lista = [1, 3, 5, 7, 9, 11, 13, 15]
objetivo = 7

print(f"\nLista ordenada: {lista}")
print(f"Buscar: {objetivo}")

resultado = busqueda_binaria(lista, objetivo)
print(f"\nResultado:")
if resultado != -1:
    print(f"  Encontrado en índice {resultado}")
else:
    print(f"  No encontrado")

print("\nAlgoritmo:")
print("  1. Comparar con elemento medio")
print("  2. Si es igual, retornar")
print("  3. Si es menor, buscar en mitad izquierda")
print("  4. Si es mayor, buscar en mitad derecha")
print("  5. Repetir hasta encontrar o agotar")

print("\nComplejidad:")
print("  Tiempo: O(log n) - Logarítmica")
print("  Espacio: O(1) - Constante")

print("\nVentajas:")
print("  ✅ Muy rápido")
print("  ✅ O(log n) - Eficiente")
print("  ✅ Mejor que búsqueda lineal")

print("\nRequisitos:")
print("  ⚠️  Lista debe estar ordenada")
print("  ⚠️  Acceso aleatorio a elementos")

print("\nCuándo usar:")
print("  - Listas grandes ordenadas")
print("  - Búsquedas frecuentes")
print("  - Cuando la velocidad importa")

print("\n" + "=" * 50)
