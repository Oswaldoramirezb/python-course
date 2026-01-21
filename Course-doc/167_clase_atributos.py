"""
CLASE: ATRIBUTOS
================
Atributos de instancia y de clase
"""

print("=" * 50)
print("ATRIBUTOS DE CLASE")
print("=" * 50)

class Persona:
    # Atributo de clase (compartido por todas las instancias)
    especie = "Homo sapiens"
    
    def __init__(self, nombre, edad):
        # Atributos de instancia (únicos para cada objeto)
        self.nombre = nombre
        self.edad = edad

print("\nAtributos de instancia:")
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

print(f"  persona1.nombre = {persona1.nombre}")
print(f"  persona2.nombre = {persona2.nombre}")

print("\nAtributo de clase (compartido):")
print(f"  Persona.especie = {Persona.especie}")
print(f"  persona1.especie = {persona1.especie}")
print(f"  persona2.especie = {persona2.especie}")

# Modificar atributo de instancia
persona1.edad = 31
print(f"\nModificar atributo de instancia:")
print(f"  persona1.edad = 31 → {persona1.edad}")
print(f"  persona2.edad sigue siendo {persona2.edad}")

print("\n" + "=" * 50)
