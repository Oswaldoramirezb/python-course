"""
DECORADOR: BUILT-IN
===================
Decoradores incorporados en Python
"""

print("=" * 50)
print("DECORADORES BUILT-IN")
print("=" * 50)

# @staticmethod
class Utilidades:
    @staticmethod
    def sumar(a, b):
        return a + b

print("\n@staticmethod:")
print(f"  Utilidades.sumar(5, 3) = {Utilidades.sumar(5, 3)}")

# @classmethod
class Persona:
    contador = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1
    
    @classmethod
    def obtener_contador(cls):
        return cls.contador

print("\n@classmethod:")
persona = Persona("Juan")
print(f"  Persona.obtener_contador() = {Persona.obtener_contador()}")

# @property
class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    
    @property
    def area(self):
        return self._ancho * self._alto

rectangulo = Rectangulo(5, 3)
print("\n@property:")
print(f"  rectangulo.area = {rectangulo.area}")

# @functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n@lru_cache:")
print(f"  fibonacci(10) = {fibonacci(10)} (cacheado)")

print("\nDecoradores built-in comunes:")
print("  @staticmethod, @classmethod, @property")
print("  @functools.lru_cache, @functools.wraps")
print("  @abc.abstractmethod")

print("\n" + "=" * 50)
