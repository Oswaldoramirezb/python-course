"""
FUNCIÓN: *ARGS
==============
Aceptar un número variable de argumentos
"""

print("=" * 50)
print("*ARGS - ARGUMENTOS VARIABLES")
print("=" * 50)

# Función con *args
def sumar_numeros(*args):
    """Suma una cantidad variable de números"""
    total = 0
    for numero in args:
        total += numero
    return total

print("\nFunción con *args:")
print(f"  sumar_numeros(1, 2, 3) = {sumar_numeros(1, 2, 3)}")
print(f"  sumar_numeros(10, 20, 30, 40, 50) = {sumar_numeros(10, 20, 30, 40, 50)}")

# Mostrar argumentos
def mostrar_info(*args):
    """Muestra información variable"""
    for i, arg in enumerate(args):
        print(f"    Argumento {i+1}: {arg}")

print(f"\nMostrar argumentos:")
print(f"  mostrar_info('Python', 'es', 'genial'):")
mostrar_info("Python", "es", "genial")

print("\n" + "=" * 50)
