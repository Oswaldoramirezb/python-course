"""
TYPE HINTS: EN CLASES
=====================
Anotaciones de tipo en clases
"""

print("=" * 50)
print("TYPE HINTS EN CLASES")
print("=" * 50)

# Clase con type hints
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
    
    def presentarse(self) -> str:
        return f"Soy {self.nombre}, tengo {self.edad} años"
    
    def cumplir_anios(self) -> None:
        self.edad += 1

print("\nClase con type hints:")
print("  class Persona:")
print("      def __init__(self, nombre: str, edad: int) -> None:")
print("          self.nombre: str = nombre")
print("          self.edad: int = edad")

persona = Persona("Juan", 30)
print(f"\nCrear objeto:")
print(f"  persona = Persona('Juan', 30)")
print(f"  persona.presentarse() = {persona.presentarse()}")

# Métodos con type hints
class Calculadora:
    @staticmethod
    def sumar(a: int, b: int) -> int:
        return a + b
    
    @classmethod
    def crear(cls) -> "Calculadora":
        return cls()

print("\nMétodos estáticos y de clase:")
print(f"  Calculadora.sumar(5, 3) = {Calculadora.sumar(5, 3)}")

print("\n" + "=" * 50)
