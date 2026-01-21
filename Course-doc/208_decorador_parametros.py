"""
DECORADOR: CON PARÁMETROS
=========================
Decoradores que aceptan parámetros
"""

print("=" * 50)
print("DECORADOR CON PARÁMETROS")
print("=" * 50)

# Decorador con parámetros
def repetir(veces):
    """Decorador que acepta parámetros"""
    def decorador(func):
        def wrapper(*args, **kwargs):
            for i in range(veces):
                print(f"  Ejecución {i+1}: {func(*args, **kwargs)}")
        return wrapper
    return decorador

@repetir(3)
def saludar(nombre):
    return f"¡Hola, {nombre}!"

print("\nDecorador con parámetros:")
print("  @repetir(3)")
print("  def saludar(nombre):")
print("      return f'¡Hola, {nombre}!'")

print("\nEjecutar:")
saludar("Juan")

# Otro ejemplo
def validar_positivos(func):
    """Valida que los argumentos sean positivos"""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Los argumentos deben ser positivos")
        return func(*args, **kwargs)
    return wrapper

@validar_positivos
def calcular_area_rectangulo(ancho, alto):
    return ancho * alto

print("\nDecorador de validación:")
print(f"  calcular_area_rectangulo(5, 3) = {calcular_area_rectangulo(5, 3)}")

print("\n" + "=" * 50)
