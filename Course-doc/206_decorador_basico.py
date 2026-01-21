"""
DECORADOR: BÁSICO
=================
Crear y usar decoradores simples
"""

print("=" * 50)
print("DECORADOR BÁSICO")
print("=" * 50)

# Decorador básico
def mi_decorador(func):
    """Decorador simple"""
    def wrapper():
        print("  Antes de ejecutar la función")
        resultado = func()
        print("  Después de ejecutar la función")
        return resultado
    return wrapper

@mi_decorador
def decir_hola():
    print("  ¡Hola!")

print("\nDecorador básico:")
print("  @mi_decorador")
print("  def decir_hola():")
print("      print('¡Hola!')")

print("\nEjecutar función decorada:")
decir_hola()

# Sin decorador (equivalente)
print("\nSin decorador (equivalente):")
def decir_hola2():
    print("  ¡Hola!")

decir_hola2 = mi_decorador(decir_hola2)
decir_hola2()

print("\n" + "=" * 50)
