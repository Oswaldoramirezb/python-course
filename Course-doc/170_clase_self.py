"""
CLASE: SELF
===========
El parámetro 'self' en métodos
"""

print("=" * 50)
print("SELF EN CLASES")
print("=" * 50)

class Persona:
    def __init__(self, nombre, edad):
        # self se refiere a la instancia actual
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        # self permite acceder a los atributos del objeto
        return f"Soy {self.nombre}, tengo {self.edad} años"
    
    def cumplir_anios(self):
        # self permite modificar el objeto
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tengo {self.edad} años"

print("\nself se refiere al objeto actual:")
persona = Persona("Juan", 30)
print(f"  persona = Persona('Juan', 30)")

print(f"\nAcceder con self:")
print(f"  persona.presentarse() = {persona.presentarse()}")

print(f"\nModificar con self:")
print(f"  persona.cumplir_anios() = {persona.cumplir_anios()}")

print("\n⚠️  IMPORTANTE:")
print("  - self es el primer parámetro de métodos de instancia")
print("  - Python lo pasa automáticamente")
print("  - Permite acceder a atributos y métodos del objeto")

print("\n" + "=" * 50)
