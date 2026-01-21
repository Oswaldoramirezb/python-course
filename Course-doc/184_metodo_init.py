"""
MÉTODO ESPECIAL: __INIT__
==========================
Constructor - inicializa el objeto
"""

print("=" * 50)
print("MÉTODO __INIT__")
print("=" * 50)

class Persona:
    def __init__(self, nombre, edad):
        """Constructor: se ejecuta al crear el objeto"""
        self.nombre = nombre
        self.edad = edad
        print(f"  ✅ Persona '{nombre}' inicializada")

print("\n__init__ se ejecuta automáticamente:")
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

print(f"\nObjetos inicializados:")
print(f"  persona1.nombre = {persona1.nombre}, edad = {persona1.edad}")
print(f"  persona2.nombre = {persona2.nombre}, edad = {persona2.edad}")

# __init__ con valores por defecto
class Persona2:
    def __init__(self, nombre, edad=0, ciudad="Desconocida"):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

persona3 = Persona2("Pedro")
print(f"\nCon valores por defecto:")
print(f"  Persona2('Pedro') → edad={persona3.edad}, ciudad='{persona3.ciudad}'")

print("\n⚠️  IMPORTANTE:")
print("  - __init__ NO es el constructor real")
print("  - __new__ es el constructor real")
print("  - __init__ es el inicializador")

print("\n" + "=" * 50)
