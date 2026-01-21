"""
GENERADOR: YIELD
================
Usar yield para crear generadores
"""

print("=" * 50)
print("GENERADOR CON YIELD")
print("=" * 50)

# Generador básico
def contar_hasta(n):
    """Generador que cuenta hasta n"""
    i = 1
    while i <= n:
        yield i
        i += 1

print("\nGenerador básico:")
print("  def contar_hasta(n):")
print("      i = 1")
print("      while i <= n:")
print("          yield i")
print("          i += 1")

print("\nUsar generador:")
for numero in contar_hasta(5):
    print(f"  {numero}")

# Generador de números pares
def numeros_pares(n):
    """Genera números pares hasta n"""
    for i in range(2, n + 1, 2):
        yield i

print("\nGenerador de pares:")
print("  numeros_pares(10):")
for par in numeros_pares(10):
    print(f"    {par}", end=" ")
print()

# Generador infinito
def numeros_infinitos():
    """Generador infinito"""
    i = 1
    while True:
        yield i
        i += 1

print("\nGenerador infinito (limitado):")
gen = numeros_infinitos()
for _ in range(5):
    print(f"  {next(gen)}", end=" ")
print()

print("\n" + "=" * 50)
