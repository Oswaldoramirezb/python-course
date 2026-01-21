"""
FUNCIÓN: ORDEN SUPERIOR
=======================
Funciones que reciben otras funciones como parámetros
"""

print("=" * 50)
print("FUNCIONES DE ORDEN SUPERIOR")
print("=" * 50)

# Función que recibe otra función
def aplicar_operacion(func, a, b):
    """Aplica una función a dos números"""
    return func(a, b)

def sumar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

print("\nFunción de orden superior:")
print(f"  aplicar_operacion(sumar, 10, 20) = {aplicar_operacion(sumar, 10, 20)}")
print(f"  aplicar_operacion(multiplicar, 6, 7) = {aplicar_operacion(multiplicar, 6, 7)}")

# Función que retorna otra función
def crear_multiplicador(factor):
    """Crea una función multiplicadora"""
    def multiplicar(numero):
        return numero * factor
    return multiplicar

multiplicar_por_2 = crear_multiplicador(2)
multiplicar_por_3 = crear_multiplicador(3)

print(f"\nFunción que retorna función:")
print(f"  multiplicar_por_2(5) = {multiplicar_por_2(5)}")
print(f"  multiplicar_por_3(5) = {multiplicar_por_3(5)}")

print("\n" + "=" * 50)
