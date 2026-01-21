"""
FUNCTOOLS: PARTIAL
==================
Crear función parcial (con algunos argumentos fijos)
"""

print("=" * 50)
print("PARTIAL - FUNCIÓN PARCIAL")
print("=" * 50)

from functools import partial

# Función original
def multiplicar(x, y, z):
    return x * y * z

print("\nFunción original:")
print("  def multiplicar(x, y, z):")
print("      return x * y * z")

# Crear función parcial
multiplicar_por_2 = partial(multiplicar, 2)
resultado = multiplicar_por_2(3, 4)
print(f"\nFijar primer argumento:")
print(f"  multiplicar_por_2 = partial(multiplicar, 2)")
print(f"  multiplicar_por_2(3, 4) = {resultado}")

# Fijar múltiples argumentos
multiplicar_2_3 = partial(multiplicar, 2, 3)
resultado2 = multiplicar_2_3(4)
print(f"\nFijar dos argumentos:")
print(f"  multiplicar_2_3 = partial(multiplicar, 2, 3)")
print(f"  multiplicar_2_3(4) = {resultado2}")

# Ejemplo práctico - Potencia
from functools import partial
potencia_2 = partial(pow, 2)
print(f"\nPotencia de 2:")
print(f"  potencia_2 = partial(pow, 2)")
print(f"  potencia_2(3) = {potencia_2(3)}")
print(f"  potencia_2(4) = {potencia_2(4)}")

print("\nVentajas:")
print("  ✅ Reutilizar funciones")
print("  ✅ Crear funciones especializadas")
print("  ✅ Simplificar llamadas")

print("\n" + "=" * 50)
