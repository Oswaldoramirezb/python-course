"""
CLASE: MÉTODOS
==============
Métodos de instancia, de clase y estáticos
"""

print("=" * 50)
print("MÉTODOS DE CLASE")
print("=" * 50)

class Persona:
    contador = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1
    
    # Método de instancia
    def presentarse(self):
        return f"Hola, soy {self.nombre}"
    
    # Método de clase
    @classmethod
    def obtener_contador(cls):
        return cls.contador
    
    # Método estático
    @staticmethod
    def es_adulto(edad):
        return edad >= 18

print("\nMétodo de instancia:")
persona = Persona("Juan")
print(f"  persona.presentarse() = {persona.presentarse()}")

print("\nMétodo de clase:")
print(f"  Persona.obtener_contador() = {Persona.obtener_contador()}")

print("\nMétodo estático:")
print(f"  Persona.es_adulto(20) = {Persona.es_adulto(20)}")
print(f"  Persona.es_adulto(15) = {Persona.es_adulto(15)}")

print("\n" + "=" * 50)
