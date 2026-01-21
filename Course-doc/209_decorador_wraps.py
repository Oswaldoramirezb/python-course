"""
DECORADOR: WRAPS
================
Preservar metadatos de la función original
"""

print("=" * 50)
print("DECORADOR CON WRAPS")
print("=" * 50)

from functools import wraps

# Sin wraps (pierde metadatos)
def decorador_sin_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorador_sin_wraps
def multiplicar(x, y):
    """Multiplica dos números"""
    return x * y

print("\nSin wraps:")
print(f"  multiplicar.__name__ = {multiplicar.__name__} (perdido)")
print(f"  multiplicar.__doc__ = {multiplicar.__doc__} (perdido)")

# Con wraps (preserva metadatos)
def decorador_con_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorador_con_wraps
def dividir(x, y):
    """Divide dos números"""
    return x / y

print("\nCon wraps:")
print(f"  dividir.__name__ = {dividir.__name__} (preservado)")
print(f"  dividir.__doc__ = {dividir.__doc__} (preservado)")

print("\nVentajas de @wraps:")
print("  ✅ Preserva __name__")
print("  ✅ Preserva __doc__")
print("  ✅ Preserva otros metadatos")
print("  ✅ Mejor para debugging")

print("\n" + "=" * 50)
