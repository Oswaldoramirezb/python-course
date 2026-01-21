"""
HERENCIA: MÚLTIPLE
==================
Herencia de múltiples clases
"""

print("=" * 50)
print("HERENCIA MÚLTIPLE")
print("=" * 50)

# Clases mixin
class Volador:
    def volar(self):
        return "Estoy volando"
    
    def aterrizar(self):
        return "Aterrizando"

class Nadador:
    def nadar(self):
        return "Estoy nadando"
    
    def sumergirse(self):
        return "Sumergiéndome"

# Clase con herencia múltiple
class Pato(Volador, Nadador):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "¡Cuac cuac!"

pato = Pato("Donald")
print("\nHerencia múltiple:")
print(f"  pato = Pato('Donald')")
print(f"  class Pato(Volador, Nadador):")

print(f"\nMétodos heredados de Volador:")
print(f"  pato.volar() = {pato.volar()}")
print(f"  pato.aterrizar() = {pato.aterrizar()}")

print(f"\nMétodos heredados de Nadador:")
print(f"  pato.nadar() = {pato.nadar()}")
print(f"  pato.sumergirse() = {pato.sumergirse()}")

print(f"\nMétodo propio:")
print(f"  pato.hacer_sonido() = {pato.hacer_sonido()}")

print("\n" + "=" * 50)
