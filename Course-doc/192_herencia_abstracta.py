"""
HERENCIA: CLASES ABSTRACTAS
===========================
Clases que no se pueden instanciar directamente
"""

print("=" * 50)
print("CLASES ABSTRACTAS")
print("=" * 50)

from abc import ABC, abstractmethod

# Clase abstracta
class Forma(ABC):
    """Clase abstracta base"""
    
    @abstractmethod
    def calcular_area(self):
        """Método abstracto que debe ser implementado"""
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        """Método abstracto que debe ser implementado"""
        pass
    
    def describir(self):
        """Método concreto (no abstracto)"""
        return f"Área: {self.calcular_area()}, Perímetro: {self.calcular_perimetro()}"

# Implementación concreta
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        import math
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        import math
        return 2 * math.pi * self.radio

print("\nClase abstracta:")
print("  from abc import ABC, abstractmethod")
print("  class Forma(ABC):")
print("      @abstractmethod")
print("      def calcular_area(self):")
print("          pass")

print("\nImplementación:")
circulo = Circulo(5)
print(f"  circulo = Circulo(5)")
print(f"  circulo.calcular_area() = {circulo.calcular_area():.2f}")
print(f"  circulo.describir() = {circulo.describir()}")

print("\n⚠️  No se puede instanciar clase abstracta:")
print("  forma = Forma() → TypeError")

print("\n" + "=" * 50)
