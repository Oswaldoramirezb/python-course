"""
EXCEPCIÓN: ¿QUÉ ES?
===================
Las excepciones son errores que ocurren durante la ejecución
"""

print("=" * 50)
print("¿QUÉ ES UNA EXCEPCIÓN?")
print("=" * 50)

print("\nUna excepción es un error que ocurre durante la ejecución:")
print("  - División por cero")
print("  - Acceder a índice que no existe")
print("  - Archivo que no existe")
print("  - Variable que no está definida")

print("\nEjemplo de error:")
print("  resultado = 10 / 0")
print("  → ZeroDivisionError: division by zero")

print("\nSin manejo de excepciones, el programa se detiene.")
print("Con manejo de excepciones, podemos controlar los errores.")

# Ejemplo práctico
print("\nEjemplo práctico:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("  ✅ Error capturado: No se puede dividir por cero")

print("\n" + "=" * 50)
