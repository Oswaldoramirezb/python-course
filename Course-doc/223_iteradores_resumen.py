"""
RESUMEN: ITERADORES
===================
Todas las operaciones con iteradores
"""

print("=" * 50)
print("RESUMEN - ITERADORES")
print("=" * 50)

print("\nConcepto:")
print("  - Objeto que permite recorrer elementos")
print("  - Implementa __iter__() y __next__()")

print("\nCrear iterador:")
print("  iterador = iter(iterable)")
print("  iterador = iter([1, 2, 3])")

print("\nObtener valores:")
print("  next(iterador)")
print("  for valor in iterador:")

print("\nIterador personalizado:")
print("  class MiIterador:")
print("      def __iter__(self):")
print("          return self")
print("")
print("      def __next__(self):")
print("          # Retorna valor o raise StopIteration")

print("\nIterable vs Iterador:")
print("  Iterable - Se puede iterar (listas, etc.)")
print("  Iterador - Produce valores (objeto con __next__)")

print("\nProtocolo:")
print("  1. iter() → __iter__()")
print("  2. next() → __next__()")
print("  3. StopIteration cuando se agota")

print("\nVentajas:")
print("  ✅ Eficiencia de memoria")
print("  ✅ Procesamiento bajo demanda")
print("  ✅ Puede ser infinito")

print("\n" + "=" * 50)
