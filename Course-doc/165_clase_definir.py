"""
CLASE: DEFINIR
==============
Crear una clase en Python
"""

print("=" * 50)
print("DEFINIR CLASES")
print("=" * 50)

# Definir clase básica
class Persona:
    """Clase que representa una persona"""
    pass

print("\nClase básica:")
print("  class Persona:")
print("      pass")

# Clase con atributos y métodos
class Persona2:
    """Clase con atributos y métodos"""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

print("\nClase completa:")
print("  class Persona2:")
print("      def __init__(self, nombre, edad):")
print("          self.nombre = nombre")
print("          self.edad = edad")
print("")
print("      def presentarse(self):")
print("          return f'Hola, soy {self.nombre}...'")

# Crear objeto
persona = Persona2("Juan", 30)
print(f"\nCrear objeto:")
print(f"  persona = Persona2('Juan', 30)")
print(f"  persona.presentarse() = {persona.presentarse()}")

print("\n" + "=" * 50)
