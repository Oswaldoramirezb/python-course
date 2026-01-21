"""
HERENCIA: BÁSICA
================
Herencia simple en Python
"""

print("=" * 50)
print("HERENCIA BÁSICA")
print("=" * 50)

# Clase padre
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        return "El animal hace un sonido"
    
    def presentarse(self):
        return f"Soy {self.nombre} y tengo {self.edad} años"

# Clase hija
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamar constructor del padre
        self.raza = raza
    
    def hacer_sonido(self):
        """Sobrescribe el método del padre"""
        return "¡Guau guau!"

print("\nClase padre: Animal")
print("Clase hija: Perro(Animal)")

perro = Perro("Max", 3, "Labrador")
print(f"\nCrear objeto:")
print(f"  perro = Perro('Max', 3, 'Labrador')")

print(f"\nMétodos heredados:")
print(f"  perro.presentarse() = {perro.presentarse()}")

print(f"\nMétodo sobrescrito:")
print(f"  perro.hacer_sonido() = {perro.hacer_sonido()}")

print(f"\nAtributo propio:")
print(f"  perro.raza = {perro.raza}")

print("\n" + "=" * 50)
