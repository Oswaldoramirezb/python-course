"""
HASHABLES: OBJETOS PERSONALIZADOS
=================================
Hacer objetos personalizados hashables
"""

print("=" * 50)
print("OBJETOS PERSONALIZADOS HASHABLES")
print("=" * 50)

# Clase hashable (inmutable)
class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __hash__(self):
        """Hash basado en coordenadas"""
        return hash((self._x, self._y))
    
    def __eq__(self, otro):
        """Igualdad basada en coordenadas"""
        if isinstance(otro, Punto):
            return self._x == otro._x and self._y == otro._y
        return False
    
    def __repr__(self):
        return f"Punto({self._x}, {self._y})"

print("\nClase hashable:")
print("  class Punto:")
print("      def __hash__(self):")
print("          return hash((self.x, self.y))")
print("      def __eq__(self, otro): ...")

punto1 = Punto(1, 2)
punto2 = Punto(1, 2)
punto3 = Punto(3, 4)

print(f"\nCrear puntos:")
print(f"  punto1 = {punto1}")
print(f"  punto2 = {punto2}")
print(f"  punto3 = {punto3}")

# Usar en set
conjunto_puntos = {punto1, punto2, punto3}
print(f"\nUsar en set:")
print(f"  {{punto1, punto2, punto3}} = {conjunto_puntos}")
print(f"  punto1 y punto2 son iguales → solo uno en el set")

# Usar como clave en dict
diccionario_puntos = {punto1: "A", punto3: "B"}
print(f"\nUsar como clave en dict:")
print(f"  {diccionario_puntos}")

print("\n⚠️  IMPORTANTE:")
print("  - Objeto debe ser inmutable")
print("  - Implementar __hash__() y __eq__()")
print("  - Hash debe ser consistente con igualdad")

print("\n" + "=" * 50)
