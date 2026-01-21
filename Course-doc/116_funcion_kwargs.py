"""
FUNCIÓN: **KWARGS
=================
Aceptar argumentos de palabra clave variables
"""

print("=" * 50)
print("**KWARGS - KEYWORD ARGUMENTS")
print("=" * 50)

# Función con **kwargs
def crear_perfil(**kwargs):
    """Crea un perfil con argumentos de palabra clave"""
    print("  Perfil creado:")
    for clave, valor in kwargs.items():
        print(f"    {clave}: {valor}")

print("\nFunción con **kwargs:")
print("  crear_perfil(nombre='Ana', edad=25, ciudad='Madrid'):")
crear_perfil(nombre="Ana", edad=25, ciudad="Madrid", profesion="Ingeniera")

# Combinación de *args y **kwargs
def funcion_completa(*args, **kwargs):
    """Acepta ambos tipos de argumentos"""
    print(f"\n  Argumentos posicionales: {args}")
    print(f"  Argumentos de palabra clave: {kwargs}")

print("\nCombinación:")
print("  funcion_completa(1, 2, 3, nombre='Juan', edad=30):")
funcion_completa(1, 2, 3, nombre="Juan", edad=30)

print("\n" + "=" * 50)
