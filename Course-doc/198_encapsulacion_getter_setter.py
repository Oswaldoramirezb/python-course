"""
ENCAPSULACIÓN: GETTER Y SETTER
===============================
Métodos para acceder y modificar atributos
"""

print("=" * 50)
print("GETTER Y SETTER")
print("=" * 50)

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    # Getter
    def get_nombre(self):
        return self._nombre
    
    # Setter
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self._nombre = nombre
        else:
            raise ValueError("Nombre debe ser una cadena no vacía")
    
    # Getter
    def get_edad(self):
        return self._edad
    
    # Setter con validación
    def set_edad(self, edad):
        if isinstance(edad, int) and 0 <= edad <= 150:
            self._edad = edad
        else:
            raise ValueError("Edad debe estar entre 0 y 150")

persona = Persona("Juan", 30)
print("\nUsar getters y setters:")
print(f"  persona.get_nombre() = {persona.get_nombre()}")
print(f"  persona.get_edad() = {persona.get_edad()}")

persona.set_edad(31)
print(f"\n  persona.set_edad(31)")
print(f"  persona.get_edad() = {persona.get_edad()}")

# Con @property (más Pythonico)
class Persona2:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str) and len(valor) > 0:
            self._nombre = valor
        else:
            raise ValueError("Nombre inválido")

persona2 = Persona2("María", 25)
print(f"\nCon @property (más Pythonico):")
print(f"  persona2.nombre = {persona2.nombre}")
persona2.nombre = "Ana"
print(f"  persona2.nombre = 'Ana' → {persona2.nombre}")

print("\n" + "=" * 50)
