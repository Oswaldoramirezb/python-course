"""
DATACLASS: BÁSICO
=================
Crear y usar dataclasses básicas
"""

print("=" * 50)
print("DATACLASS BÁSICO")
print("=" * 50)

from dataclasses import dataclass

# Dataclass básica
@dataclass
class Persona:
    nombre: str
    edad: int
    ciudad: str = "Desconocida"  # Valor por defecto

print("\nDataclass básica:")
print("  @dataclass")
print("  class Persona:")
print("      nombre: str")
print("      edad: int")
print("      ciudad: str = 'Desconocida'")

persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25, "Madrid")

print("\nCrear objetos:")
print(f"  persona1 = {persona1}")
print(f"  persona2 = {persona2}")

print("\nMétodos automáticos:")
print(f"  repr(persona1) = {repr(persona1)}")
print(f"  persona1 == persona2 = {persona1 == persona2}")

# Comparar con clase normal
class PersonaNormal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona_normal = PersonaNormal("Juan", 30)
print(f"\nClase normal:")
print(f"  repr(persona_normal) = {repr(persona_normal)}")

print("\n" + "=" * 50)
