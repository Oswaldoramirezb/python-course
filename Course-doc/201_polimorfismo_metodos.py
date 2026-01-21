"""
POLIMORFISMO: MÉTODOS
=====================
Polimorfismo mediante sobrescritura de métodos
"""

print("=" * 50)
print("POLIMORFISMO CON MÉTODOS")
print("=" * 50)

class Animal:
    def hacer_sonido(self):
        return "El animal hace un sonido"

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau miau!"

class Pato(Animal):
    def hacer_sonido(self):
        return "¡Cuac cuac!"

print("\nPolimorfismo:")
perro = Perro()
gato = Gato()
pato = Pato()

print(f"  perro.hacer_sonido() = {perro.hacer_sonido()}")
print(f"  gato.hacer_sonido() = {gato.hacer_sonido()}")
print(f"  pato.hacer_sonido() = {pato.hacer_sonido()}")

# Función polimórfica
def hacer_ruido_animal(animal):
    """Función que demuestra polimorfismo"""
    return animal.hacer_sonido()

print("\nFunción polimórfica:")
animales = [perro, gato, pato]
for animal in animales:
    print(f"  {hacer_ruido_animal(animal)}")

print("\nMismo método, diferentes comportamientos según el objeto")

print("\n" + "=" * 50)
