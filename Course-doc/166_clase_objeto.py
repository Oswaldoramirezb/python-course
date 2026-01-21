"""
CLASE: OBJETO
=============
Crear objetos (instancias) de una clase
"""

print("=" * 50)
print("CREAR OBJETOS")
print("=" * 50)

# Definir clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años"

# Crear objetos
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

print("\nCrear objetos:")
print(f"  persona1 = Persona('Juan', 30)")
print(f"  persona2 = Persona('María', 25)")

print("\nCada objeto es independiente:")
print(f"  persona1.nombre = {persona1.nombre}")
print(f"  persona2.nombre = {persona2.nombre}")

print("\nLlamar métodos:")
print(f"  persona1.presentarse() = {persona1.presentarse()}")
print(f"  persona2.presentarse() = {persona2.presentarse()}")

print("\nVerificar tipo:")
print(f"  type(persona1) = {type(persona1).__name__}")
print(f"  isinstance(persona1, Persona) = {isinstance(persona1, Persona)}")

print("\n" + "=" * 50)
