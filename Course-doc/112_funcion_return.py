"""
FUNCIÓN: RETURN
===============
Retornar valores de una función
"""

print("=" * 50)
print("RETURN EN FUNCIONES")
print("=" * 50)

# Función con return
def sumar(a, b):
    """Retorna la suma de dos números"""
    return a + b

resultado = sumar(5, 3)
print(f"\nFunción con return:")
print(f"  def sumar(a, b):")
print(f"      return a + b")
print(f"  resultado = sumar(5, 3) = {resultado}")

# Función sin return (retorna None)
def saludar(nombre):
    print(f"Hola, {nombre}!")

resultado2 = saludar("Juan")
print(f"\nFunción sin return:")
print(f"  resultado = {resultado2} (None)")

# Múltiples returns
def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

print(f"\nMúltiples returns:")
print(f"  es_par(4) = {es_par(4)}")
print(f"  es_par(5) = {es_par(5)}")

print("\n" + "=" * 50)
