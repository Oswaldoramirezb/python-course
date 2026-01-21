"""
ENCAPSULACIÓN: PROTEGIDO
========================
Atributos protegidos (convención: _atributo)
"""

print("=" * 50)
print("ENCAPSULACIÓN PROTEGIDA")
print("=" * 50)

class Persona:
    def __init__(self, nombre, edad):
        # Atributo protegido (convención: un guion bajo)
        self._nombre = nombre
        self._edad = edad
    
    def obtener_nombre(self):
        return self._nombre
    
    def establecer_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("  ⚠️  Edad debe ser positiva")

persona = Persona("Juan", 30)
print("\nAtributos protegidos (convención):")
print(f"  self._nombre = '{persona._nombre}'")
print(f"  self._edad = {persona._edad}")

print("\nAcceso:")
print("  ⚠️  Convención: No acceder directamente")
print("  ✅ Usar métodos getter/setter")
print(f"  persona.obtener_nombre() = {persona.obtener_nombre()}")

print("\n⚠️  IMPORTANTE:")
print("  - Es solo una convención")
print("  - Python NO impide el acceso")
print("  - Indica 'no usar directamente'")

print("\n" + "=" * 50)
