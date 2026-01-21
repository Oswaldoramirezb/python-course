"""
PAQUETE: __INIT__.PY
====================
Archivo de inicialización de paquetes
"""

print("=" * 50)
print("__INIT__.PY")
print("=" * 50)

# __init__.py puede estar vacío
print("\n__init__.py puede estar vacío:")
print("  # Archivo vacío")
print("  # Solo marca la carpeta como paquete")

# __init__.py con código
print("\n__init__.py con código:")
print("  # Puede importar módulos del paquete")
print("  from .modulo1 import funcion1")
print("  from .modulo2 import funcion2")
print("")
print("  # Facilita importaciones:")
print("  from mi_paquete import funcion1, funcion2")

# __all__
print("\n__all__ - controlar importaciones:")
print("  __all__ = ['funcion1', 'funcion2']")
print("  # Define qué se importa con 'from paquete import *'")

# Ejemplo práctico
print("\nEjemplo - mi_paquete/__init__.py:")
print("  from .modulo1 import saludar")
print("  from .modulo2 import sumar")
print("")
print("  __all__ = ['saludar', 'sumar']")

print("\nUso:")
print("  from mi_paquete import saludar, sumar")
print("  # O")
print("  from mi_paquete import *")

print("\n" + "=" * 50)
