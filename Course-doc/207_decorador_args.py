"""
DECORADOR: CON ARGUMENTOS
=========================
Decoradores que manejan funciones con argumentos
"""

print("=" * 50)
print("DECORADOR CON ARGUMENTOS")
print("=" * 50)

# Decorador que maneja argumentos
def decorador_con_args(func):
    """Decorador que maneja funciones con argumentos"""
    def wrapper(*args, **kwargs):
        print(f"  Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"  Resultado: {resultado}")
        return resultado
    return wrapper

@decorador_con_args
def sumar(a, b):
    return a + b

print("\nDecorador con argumentos:")
print("  @decorador_con_args")
print("  def sumar(a, b):")
print("      return a + b")

print("\nLlamar función decorada:")
resultado = sumar(5, 3)
print(f"  sumar(5, 3) = {resultado}")

# Con múltiples argumentos
@decorador_con_args
def saludar(nombre, edad, ciudad="Desconocida"):
    return f"Hola, {nombre}, {edad} años, de {ciudad}"

print("\nCon múltiples argumentos:")
saludar("Juan", 30, ciudad="Madrid")

print("\n" + "=" * 50)
