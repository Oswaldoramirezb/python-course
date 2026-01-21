"""
FUNCIÓN: DOCSTRING
==================
Documentar funciones
"""

print("=" * 50)
print("DOCSTRINGS")
print("=" * 50)

# Función con docstring
def calcular_area_rectangulo(ancho, alto):
    """
    Calcula el área de un rectángulo.
    
    Args:
        ancho: Ancho del rectángulo
        alto: Alto del rectángulo
    
    Returns:
        El área del rectángulo
    """
    return ancho * alto

print("\nFunción con docstring:")
print("  def calcular_area_rectangulo(ancho, alto):")
print("      '''Calcula el área de un rectángulo...'''")
print("      return ancho * alto")

# Acceder al docstring
print(f"\nVer docstring:")
print(f"  calcular_area_rectangulo.__doc__")
print(f"  {calcular_area_rectangulo.__doc__}")

# Usar help()
print(f"\nUsar help():")
print("  help(calcular_area_rectangulo)")

area = calcular_area_rectangulo(5, 3)
print(f"\nEjemplo: calcular_area_rectangulo(5, 3) = {area}")

print("\n" + "=" * 50)
