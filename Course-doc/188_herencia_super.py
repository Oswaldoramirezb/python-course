"""
HERENCIA: SUPER
===============
Usar super() para acceder a la clase padre
"""

print("=" * 50)
print("SUPER()")
print("=" * 50)

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        return "El animal hace un sonido"

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # super() llama al método de la clase padre
        super().__init__(nombre, edad)
        self.raza = raza
    
    def hacer_sonido(self):
        # Llamar método del padre y extenderlo
        sonido_padre = super().hacer_sonido()
        return f"{sonido_padre} - ¡Guau guau!"

print("\nUsar super() en constructor:")
perro = Perro("Max", 3, "Labrador")
print(f"  perro = Perro('Max', 3, 'Labrador')")
print(f"  perro.nombre = {perro.nombre} (heredado)")
print(f"  perro.raza = {perro.raza} (propio)")

print("\nUsar super() en métodos:")
print(f"  perro.hacer_sonido() = {perro.hacer_sonido()}")

print("\nVentajas de super():")
print("  ✅ Accede a métodos de la clase padre")
print("  ✅ Funciona con herencia múltiple")
print("  ✅ Mantiene el orden de resolución (MRO)")

print("\n" + "=" * 50)
