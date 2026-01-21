"""
DESCRIPTORS: IMPLEMENTAR
========================
Crear descriptors personalizados
"""

print("=" * 50)
print("IMPLEMENTAR DESCRIPTORS")
print("=" * 50)

# Descriptor básico
class DescriptorSimple:
    """Descriptor simple"""
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.nombre)
    
    def __set__(self, instance, value):
        instance.__dict__[self.nombre] = value
    
    def __delete__(self, instance):
        del instance.__dict__[self.nombre]

# Usar descriptor
class Persona:
    nombre = DescriptorSimple("nombre")
    edad = DescriptorSimple("edad")
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

print("\nDescriptor básico:")
print("  class DescriptorSimple:")
print("      def __get__(self, instance, owner): ...")
print("      def __set__(self, instance, value): ...")

persona = Persona("Juan", 30)
print(f"\nUsar:")
print(f"  persona = Persona('Juan', 30)")
print(f"  persona.nombre = {persona.nombre}")
print(f"  persona.edad = {persona.edad}")

# Descriptor con validación
class EdadDescriptor:
    """Descriptor con validación"""
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.nombre)
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Edad debe ser un entero")
        if value < 0 or value > 150:
            raise ValueError("Edad debe estar entre 0 y 150")
        instance.__dict__[self.nombre] = value

class PersonaValidada:
    edad = EdadDescriptor("edad")
    
    def __init__(self, edad):
        self.edad = edad

print("\nDescriptor con validación:")
print("  class EdadDescriptor:")
print("      def __set__(self, instance, value):")
print("          if not isinstance(value, int):")
print("              raise TypeError(...)")

persona2 = PersonaValidada(30)
print(f"  persona2.edad = {persona2.edad}")

try:
    persona2.edad = 200
except ValueError as e:
    print(f"  Error: {e}")

print("\nVentajas:")
print("  ✅ Validación automática")
print("  ✅ Reutilizable")
print("  ✅ Control fino")

print("\n" + "=" * 50)
