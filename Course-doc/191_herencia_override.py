"""
HERENCIA: OVERRIDE
==================
Sobrescribir métodos de la clase padre
"""

print("=" * 50)
print("OVERRIDE - SOBRESCRIBIR MÉTODOS")
print("=" * 50)

class Animal:
    def hacer_sonido(self):
        return "El animal hace un sonido"
    
    def moverse(self):
        return "El animal se mueve"

class Perro(Animal):
    def hacer_sonido(self):
        """Sobrescribe el método del padre"""
        return "¡Guau guau!"

class Gato(Animal):
    def hacer_sonido(self):
        """Sobrescribe el método del padre"""
        return "¡Miau miau!"
    
    def moverse(self):
        """Sobrescribe y extiende"""
        movimiento_base = super().moverse()
        return f"{movimiento_base} - El gato camina sigilosamente"

print("\nOverride básico:")
perro = Perro()
print(f"  perro.hacer_sonido() = {perro.hacer_sonido()}")

print("\nOverride con super():")
gato = Gato()
print(f"  gato.hacer_sonido() = {gato.hacer_sonido()}")
print(f"  gato.moverse() = {gato.moverse()}")

print("\nComparación:")
animal = Animal()
print(f"  animal.hacer_sonido() = {animal.hacer_sonido()}")
print(f"  perro.hacer_sonido() = {perro.hacer_sonido()} (sobrescrito)")

print("\n" + "=" * 50)
