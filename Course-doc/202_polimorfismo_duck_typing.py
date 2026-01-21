"""
POLIMORFISMO: DUCK TYPING
=========================
'Si camina como pato y suena como pato, es un pato'
"""

print("=" * 50)
print("DUCK TYPING")
print("=" * 50)

print("\nDuck Typing:")
print("  'Si camina como pato y suena como pato, es un pato'")
print("  No importa el tipo, importa el comportamiento")

# Clases sin herencia común
class Perro:
    def hacer_sonido(self):
        return "¡Guau guau!"

class Gato:
    def hacer_sonido(self):
        return "¡Miau miau!"

class Reloj:
    def hacer_sonido(self):
        return "¡Tic tac!"

print("\nClases sin herencia común:")
print("  class Perro:")
print("      def hacer_sonido(self): ...")
print("")
print("  class Gato:")
print("      def hacer_sonido(self): ...")
print("")
print("  class Reloj:")
print("      def hacer_sonido(self): ...")

# Función que funciona con cualquier objeto que tenga hacer_sonido()
def hacer_ruido(objeto):
    """Funciona con cualquier objeto que tenga hacer_sonido()"""
    return objeto.hacer_sonido()

perro = Perro()
gato = Gato()
reloj = Reloj()

print("\nFunción polimórfica (duck typing):")
print(f"  hacer_ruido(perro) = {hacer_ruido(perro)}")
print(f"  hacer_ruido(gato) = {hacer_ruido(gato)}")
print(f"  hacer_ruido(reloj) = {hacer_ruido(reloj)}")

print("\nVentajas:")
print("  ✅ No requiere herencia")
print("  ✅ Código más flexible")
print("  ✅ Enfoque Pythonico")

print("\n" + "=" * 50)
