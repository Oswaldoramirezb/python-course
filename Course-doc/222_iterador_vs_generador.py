"""
ITERADOR: VS GENERADOR
======================
Diferencias entre iteradores y generadores
"""

print("=" * 50)
print("ITERADOR VS GENERADOR")
print("=" * 50)

# Iterador (clase)
class ContadorIterador:
    def __init__(self, limite):
        self.limite = limite
        self.actual = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.actual < self.limite:
            self.actual += 1
            return self.actual
        raise StopIteration

# Generador (función)
def contador_generador(limite):
    actual = 1
    while actual <= limite:
        yield actual
        actual += 1

print("\nIterador (clase):")
print("  class ContadorIterador:")
print("      def __iter__(self): ...")
print("      def __next__(self): ...")

print("\nGenerador (función):")
print("  def contador_generador(limite):")
print("      yield valor")

print("\nAmbos funcionan igual:")
iterador = ContadorIterador(3)
generador = contador_generador(3)

print("\nCon iterador:")
for num in iterador:
    print(f"  {num}")

print("\nCon generador:")
for num in generador:
    print(f"  {num}")

print("\nDiferencias:")
print("  Iterador:")
print("    - Implementa __iter__ y __next__")
print("    - Más código")
print("    - Más control")
print("")
print("  Generador:")
print("    - Usa yield")
print("    - Menos código")
print("    - Más simple")

print("\n" + "=" * 50)
