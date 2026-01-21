"""
RESUMEN: HERENCIA
=================
Todas las operaciones con herencia
"""

print("=" * 50)
print("RESUMEN - HERENCIA")
print("=" * 50)

print("\nHerencia básica:")
print("  class ClaseHija(ClasePadre):")
print("      def __init__(self):")
print("          super().__init__()")

print("\nVentajas:")
print("  ✅ Reutilización de código")
print("  ✅ Organización jerárquica")
print("  ✅ Extensibilidad")

print("\nOperaciones:")
print("  - Herencia simple: class Hija(Padre)")
print("  - Herencia múltiple: class Hija(Padre1, Padre2)")
print("  - super() - Acceder a clase padre")
print("  - Override - Sobrescribir métodos")
print("  - Clases abstractas - ABC, @abstractmethod")

print("\nMRO (Method Resolution Order):")
print("  - Orden de búsqueda de métodos")
print("  - Clase.__mro__ para ver el orden")

print("\nEjemplo completo:")
print("  class Animal:")
print("      def hacer_sonido(self):")
print("          return 'Sonido'")
print("")
print("  class Perro(Animal):")
print("      def hacer_sonido(self):")
print("          return 'Guau'")

print("\n" + "=" * 50)
