"""
ENCAPSULACIÓN: PÚBLICO
======================
Atributos y métodos públicos (acceso libre)
"""

print("=" * 50)
print("ENCAPSULACIÓN PÚBLICA")
print("=" * 50)

class Persona:
    def __init__(self, nombre, edad):
        # Atributos públicos (sin prefijo)
        self.nombre = nombre
        self.edad = edad
    
    # Método público
    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años"

persona = Persona("Juan", 30)
print("\nAtributos públicos:")
print(f"  persona.nombre = {persona.nombre}")
print(f"  persona.edad = {persona.edad}")

print("\nMétodos públicos:")
print(f"  persona.presentarse() = {persona.presentarse()}")

print("\nAcceso libre:")
print("  ✅ Se puede leer")
print("  ✅ Se puede modificar")
print("  ✅ Accesible desde cualquier lugar")

# Modificar directamente
persona.edad = 31
print(f"\nModificar directamente:")
print(f"  persona.edad = 31 → {persona.edad}")

print("\n" + "=" * 50)
