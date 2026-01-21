"""
MÉTODO ESPECIAL: __SUB__
=========================
Sobrecargar el operador -
"""

print("=" * 50)
print("MÉTODO __SUB__")
print("=" * 50)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, otro):
        """Sobrecarga el operador -"""
        return Vector(self.x - otro.x, self.y - otro.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(5, 7)
v2 = Vector(2, 3)

print("\nSobrecargar operador -:")
print(f"  v1 = {v1}")
print(f"  v2 = {v2}")

v3 = v1 - v2
print(f"  v1 - v2 = {v3}")

# Ejemplo con números
class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def __sub__(self, otro):
        if isinstance(otro, Numero):
            return Numero(self.valor - otro.valor)
        return Numero(self.valor - otro)
    
    def __str__(self):
        return str(self.valor)

n1 = Numero(10)
n2 = Numero(3)
print(f"\nCon números:")
print(f"  n1 - n2 = {n1 - n2}")

print("\n" + "=" * 50)
