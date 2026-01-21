"""
ITERADOR: CONCEPTO
==================
¿Qué es un iterador?
"""

print("=" * 50)
print("CONCEPTO DE ITERADORES")
print("=" * 50)

print("\nIterador:")
print("  - Objeto que permite recorrer elementos")
print("  - Implementa __iter__() y __next__()")
print("  - Se usa con for, next(), etc.")

print("\nIterable vs Iterador:")
print("  Iterable - Objeto que se puede iterar (listas, tuplas, etc.)")
print("  Iterador - Objeto que produce valores uno a uno")

print("\nEjemplo:")
print("  lista = [1, 2, 3]  # Iterable")
print("  iterador = iter(lista)  # Iterador")
print("  next(iterador)  # 1")
print("  next(iterador)  # 2")

print("\nProtocolo de iteración:")
print("  1. iter() llama a __iter__()")
print("  2. next() llama a __next__()")
print("  3. StopIteration cuando se agota")

print("\nObjetos iterables en Python:")
print("  ✅ Listas, tuplas, diccionarios, sets")
print("  ✅ Cadenas")
print("  ✅ Archivos")
print("  ✅ Generadores")

print("\nVentajas:")
print("  ✅ Eficiencia de memoria")
print("  ✅ Procesamiento bajo demanda")
print("  ✅ Puede ser infinito")

print("\n" + "=" * 50)
