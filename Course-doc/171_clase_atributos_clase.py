"""
CLASE: ATRIBUTOS DE CLASE
=========================
Atributos compartidos por todas las instancias
"""

print("=" * 50)
print("ATRIBUTOS DE CLASE")
print("=" * 50)

class Persona:
    # Atributo de clase
    especie = "Homo sapiens"
    contador = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

print("\nAtributo de clase (compartido):")
persona1 = Persona("Juan")
persona2 = Persona("María")

print(f"  Persona.especie = {Persona.especie}")
print(f"  persona1.especie = {persona1.especie}")
print(f"  persona2.especie = {persona2.especie}")

print("\nModificar atributo de clase afecta a todos:")
Persona.especie = "Homo sapiens sapiens"
print(f"  Persona.especie = '{Persona.especie}'")
print(f"  persona1.especie = '{persona1.especie}'")

print("\nContador compartido:")
print(f"  Persona.contador = {Persona.contador}")
print(f"  (se incrementa cada vez que se crea un objeto)")

print("\n" + "=" * 50)
