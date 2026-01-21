"""
FUNCIÓN: LLAMAR
===============
Ejecutar una función
"""

print("=" * 50)
print("LLAMAR FUNCIONES")
print("=" * 50)

# Definir función
def sumar(a, b):
    """Suma dos números"""
    return a + b

print("\nFunción definida:")
print("  def sumar(a, b):")
print("      return a + b")

# Llamar función
resultado = sumar(5, 3)
print(f"\nLlamar función:")
print(f"  resultado = sumar(5, 3)")
print(f"  resultado = {resultado}")

# Llamar directamente
print(f"\nLlamar directamente:")
print(f"  sumar(10, 20) = {sumar(10, 20)}")

# Llamar múltiples veces
print(f"\nLlamar múltiples veces:")
print(f"  sumar(1, 2) = {sumar(1, 2)}")
print(f"  sumar(100, 200) = {sumar(100, 200)}")

print("\n" + "=" * 50)
