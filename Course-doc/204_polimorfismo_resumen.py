"""
RESUMEN: POLIMORFISMO
=====================
Todas las operaciones con polimorfismo
"""

print("=" * 50)
print("RESUMEN - POLIMORFISMO")
print("=" * 50)

print("\nConcepto:")
print("  - 'Muchas formas'")
print("  - Mismo método, diferentes comportamientos")
print("  - Depende del tipo de objeto")

print("\nTipos:")
print("  1. Polimorfismo de métodos (override)")
print("  2. Duck typing")
print("  3. Polimorfismo con interfaces")

print("\nEjemplo - Polimorfismo de métodos:")
print("  class Animal:")
print("      def hacer_sonido(self): ...")
print("")
print("  class Perro(Animal):")
print("      def hacer_sonido(self): return 'Guau'")
print("")
print("  class Gato(Animal):")
print("      def hacer_sonido(self): return 'Miau'")

print("\nEjemplo - Duck typing:")
print("  def funcion(objeto):")
print("      objeto.metodo()  # No importa el tipo")

print("\nEjemplo - Interfaces:")
print("  class Forma(ABC):")
print("      @abstractmethod")
print("      def calcular_area(self): pass")

print("\nVentajas:")
print("  ✅ Código flexible")
print("  ✅ Reutilización")
print("  ✅ Extensibilidad")

print("\n" + "=" * 50)
