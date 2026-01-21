"""
CLASE: PROPIEDADES (@PROPERTY)
==============================
Atributos con getters y setters
"""

print("=" * 50)
print("PROPIEDADES (@PROPERTY)")
print("=" * 50)

class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho  # Atributo protegido
        self._alto = alto
    
    @property
    def ancho(self):
        """Getter para ancho"""
        return self._ancho
    
    @ancho.setter
    def ancho(self, valor):
        """Setter para ancho con validación"""
        if valor > 0:
            self._ancho = valor
        else:
            raise ValueError("El ancho debe ser positivo")
    
    @property
    def area(self):
        """Propiedad calculada (solo lectura)"""
        return self._ancho * self._alto

print("\nPropiedades con @property:")
rectangulo = Rectangulo(5, 3)
print(f"  rectangulo = Rectangulo(5, 3)")

print(f"\nUsar como atributo:")
print(f"  rectangulo.ancho = {rectangulo.ancho}")
print(f"  rectangulo.area = {rectangulo.area}")

print(f"\nModificar con setter:")
rectangulo.ancho = 10
print(f"  rectangulo.ancho = 10 → {rectangulo.ancho}")

print("\nVentajas:")
print("  ✅ Validación automática")
print("  ✅ Sintaxis como atributo")
print("  ✅ Propiedades calculadas")

print("\n" + "=" * 50)
