"""
POLIMORFISMO: INTERFACES
========================
Polimorfismo mediante interfaces (clases abstractas)
"""

print("=" * 50)
print("POLIMORFISMO CON INTERFACES")
print("=" * 50)

from abc import ABC, abstractmethod

# Interfaz (clase abstracta)
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

# Implementaciones
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        import math
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        import math
        return 2 * math.pi * self.radio

print("\nInterfaz (clase abstracta):")
print("  class Forma(ABC):")
print("      @abstractmethod")
print("      def calcular_area(self): pass")

print("\nImplementaciones:")
rectangulo = Rectangulo(5, 3)
circulo = Circulo(5)

formas = [rectangulo, circulo]
print("\nPolimorfismo con interfaz:")
for forma in formas:
    print(f"  Área: {forma.calcular_area():.2f}, Perímetro: {forma.calcular_perimetro():.2f}")

print("\nVentajas:")
print("  ✅ Garantiza que todas las formas tengan los métodos")
print("  ✅ Código más seguro")
print("  ✅ Documentación clara de la interfaz")

print("\n" + "=" * 50)
