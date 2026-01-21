"""
ITERADOR: PERSONALIZADO
=======================
Crear tu propio iterador
"""

print("=" * 50)
print("ITERADOR PERSONALIZADO")
print("=" * 50)

# Iterador personalizado
class Contador:
    """Iterador que cuenta hasta un límite"""
    def __init__(self, limite):
        self.limite = limite
        self.actual = 0
    
    def __iter__(self):
        """Retorna el iterador (self)"""
        return self
    
    def __next__(self):
        """Retorna el siguiente valor"""
        if self.actual < self.limite:
            self.actual += 1
            return self.actual
        else:
            raise StopIteration

print("\nIterador personalizado:")
print("  class Contador:")
print("      def __iter__(self):")
print("          return self")
print("")
print("      def __next__(self):")
print("          # Retorna siguiente valor")
print("          # O raise StopIteration")

contador = Contador(5)
print("\nUsar iterador:")
for numero in contador:
    print(f"  {numero}")

# Con next()
contador2 = Contador(3)
print("\nCon next():")
print(f"  next(contador2) = {next(contador2)}")
print(f"  next(contador2) = {next(contador2)}")
print(f"  next(contador2) = {next(contador2)}")

print("\n" + "=" * 50)
