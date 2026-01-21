"""
TYPE HINTS: BÁSICOS
====================
Anotaciones de tipo básicas
"""

print("=" * 50)
print("TYPE HINTS BÁSICOS")
print("=" * 50)

# Variables con type hints
nombre: str = "Juan"
edad: int = 30
altura: float = 1.75
activo: bool = True

print("\nVariables con type hints:")
print(f"  nombre: str = '{nombre}'")
print(f"  edad: int = {edad}")
print(f"  altura: float = {altura}")
print(f"  activo: bool = {activo}")

# Funciones con type hints
def sumar(a: int, b: int) -> int:
    """Suma dos números enteros"""
    return a + b

print("\nFunciones con type hints:")
print("  def sumar(a: int, b: int) -> int:")
print("      return a + b")

resultado = sumar(5, 3)
print(f"  sumar(5, 3) = {resultado}")

# Múltiples tipos
def procesar(valor: str | int) -> str:
    """Acepta str o int"""
    return str(valor)

print("\nMúltiples tipos (Python 3.10+):")
print("  def procesar(valor: str | int) -> str:")
print(f"  procesar('texto') = {procesar('texto')}")
print(f"  procesar(123) = {procesar(123)}")

print("\n" + "=" * 50)
