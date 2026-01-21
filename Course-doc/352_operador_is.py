"""
OPERADOR: IS
============
Verificar identidad de objetos
"""

print("=" * 50)
print("OPERADOR IS")
print("=" * 50)

# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"\nListas:")
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  c = a")

print(f"\nComparación:")
print(f"  a == b = {a == b}  # Valores iguales")
print(f"  a is b = {a is b}  # Mismo objeto? No")
print(f"  a is c = {a is c}  # Mismo objeto? Sí")

# Con enteros pequeños (cached)
x = 5
y = 5
print(f"\nEnteros pequeños (cached):")
print(f"  x = 5, y = 5")
print(f"  x is y = {x is y}  # True (Python cachea enteros pequeños)")

# Con None
valor = None
print(f"\nCon None:")
print(f"  valor is None = {valor is None}")
print(f"  valor == None = {valor == None}  # Funciona pero no recomendado")

# Comparar objetos
class MiClase:
    def __init__(self, valor):
        self.valor = valor
    
    def __eq__(self, otro):
        return self.valor == otro.valor

obj1 = MiClase(10)
obj2 = MiClase(10)
obj3 = obj1

print(f"\nCon objetos:")
print(f"  obj1 == obj2 = {obj1 == obj2}  # Valores iguales")
print(f"  obj1 is obj2 = {obj1 is obj2}  # Mismo objeto? No")
print(f"  obj1 is obj3 = {obj1 is obj3}  # Mismo objeto? Sí")

# id() para ver identidad
print(f"\nIdentidad (id):")
print(f"  id(a) = {id(a)}")
print(f"  id(b) = {id(b)}")
print(f"  id(c) = {id(c)}")
print(f"  a is c = {id(a) == id(c)}")

print("\nDiferencia:")
print("  == - Compara valores")
print("  is - Compara identidad (mismo objeto)")

print("\nCuándo usar is:")
print("  ✅ Comparar con None: if valor is None")
print("  ✅ Verificar si es el mismo objeto")
print("  ✅ Comparar con True/False (aunque == también funciona)")

print("\n" + "=" * 50)
