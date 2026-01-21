"""
PERFORMANCE: TIMEIT
===================
Medir tiempo de ejecución
"""

print("=" * 50)
print("TIMEIT - MEDIR TIEMPO")
print("=" * 50)

import timeit

# Función a medir
def sumar_lista(lista):
    """Sumar elementos de lista"""
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

def sumar_builtin(lista):
    """Sumar con built-in"""
    return sum(lista)

print("\nMedir tiempo con timeit:")
print("  import timeit")
print("  tiempo = timeit.timeit('código', number=1000)")

# Medir tiempo
lista = list(range(1000))

tiempo1 = timeit.timeit(lambda: sumar_lista(lista), number=1000)
tiempo2 = timeit.timeit(lambda: sumar_builtin(lista), number=1000)

print(f"\nComparación:")
print(f"  sumar_lista(): {tiempo1:.6f} segundos")
print(f"  sum() built-in: {tiempo2:.6f} segundos")
print(f"  Diferencia: {tiempo1/tiempo2:.2f}x más lento")

# timeit con setup
print("\ntimeit con setup:")
codigo = "sum(lista)"
setup = "lista = list(range(1000))"
tiempo = timeit.timeit(codigo, setup=setup, number=10000)
print(f"  Tiempo: {tiempo:.6f} segundos")

# Comparar múltiples versiones
print("\nComparar versiones:")
versiones = {
    "Bucle for": "suma = 0; [suma := suma + x for x in range(1000)]",
    "sum()": "sum(range(1000))",
    "reduce": "from functools import reduce; reduce(lambda x, y: x + y, range(1000))"
}

for nombre, codigo in versiones.items():
    tiempo = timeit.timeit(codigo, number=10000)
    print(f"  {nombre}: {tiempo:.6f} segundos")

print("\nVentajas:")
print("  ✅ Precisión")
print("  ✅ Múltiples ejecuciones")
print("  ✅ Comparación fácil")

print("\n" + "=" * 50)
