"""
EXCEPCIÓN: TIPOS COMUNES
========================
Tipos de excepciones más comunes
"""

print("=" * 50)
print("TIPOS DE EXCEPCIONES")
print("=" * 50)

print("\nExcepciones comunes:")
print("  ZeroDivisionError - División por cero")
print("  ValueError - Valor incorrecto")
print("  TypeError - Tipo de dato incorrecto")
print("  IndexError - Índice fuera de rango")
print("  KeyError - Clave no existe en diccionario")
print("  FileNotFoundError - Archivo no encontrado")
print("  NameError - Variable no definida")

# Ejemplos
print("\nEjemplos:")

# ZeroDivisionError
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"  ZeroDivisionError: {e}")

# ValueError
try:
    numero = int("abc")
except ValueError as e:
    print(f"  ValueError: {e}")

# IndexError
try:
    lista = [1, 2, 3]
    elemento = lista[10]
except IndexError as e:
    print(f"  IndexError: {e}")

# KeyError
try:
    diccionario = {"a": 1}
    valor = diccionario["b"]
except KeyError as e:
    print(f"  KeyError: {e}")

print("\n" + "=" * 50)
