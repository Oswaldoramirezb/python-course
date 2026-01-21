"""
CLASE: CONSTRUCTOR
==================
Método __init__ para inicializar objetos
"""

print("=" * 50)
print("CONSTRUCTOR __INIT__")
print("=" * 50)

class Persona:
    def __init__(self, nombre, edad):
        """Constructor: se ejecuta al crear el objeto"""
        self.nombre = nombre
        self.edad = edad
        print(f"  ✅ Persona '{nombre}' creada")

print("\nConstructor se ejecuta automáticamente:")
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

print(f"\nObjetos creados:")
print(f"  persona1.nombre = {persona1.nombre}, edad = {persona1.edad}")
print(f"  persona2.nombre = {persona2.nombre}, edad = {persona2.edad}")

# Constructor con valores por defecto
class Persona2:
    def __init__(self, nombre, edad=0):
        self.nombre = nombre
        self.edad = edad

persona3 = Persona2("Pedro")
print(f"\nCon valor por defecto:")
print(f"  Persona2('Pedro') → edad = {persona3.edad}")

print("\n" + "=" * 50)
