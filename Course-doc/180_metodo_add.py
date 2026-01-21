"""
MÉTODO ESPECIAL: __ADD__
=========================
Sobrecargar el operador +
"""

print("=" * 50)
print("MÉTODO __ADD__")
print("=" * 50)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        """Sobrecarga el operador +"""
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("\nSobrecargar operador +:")
print(f"  v1 = {v1}")
print(f"  v2 = {v2}")

v3 = v1 + v2
print(f"  v1 + v2 = {v3}")

print("\nSin __add__:")
print("  v1 + v2 → TypeError")

print("\nCon __add__:")
print("  v1 + v2 → Vector(4, 6)")

print("\n" + "=" * 50)
