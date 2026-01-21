"""
EXCEPCIÓN: TRY-EXCEPT
======================
Capturar y manejar excepciones
"""

print("=" * 50)
print("TRY-EXCEPT")
print("=" * 50)

# try-except básico
print("\nEjemplo 1 - División por cero:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("  ✅ Error capturado: No se puede dividir por cero")

# try-except con resultado
print("\nEjemplo 2 - Función con manejo de errores:")
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"

print(f"  dividir(10, 2) = {dividir(10, 2)}")
print(f"  dividir(10, 0) = {dividir(10, 0)}")

# try-except con múltiples excepciones
print("\nEjemplo 3 - Múltiples excepciones:")
def convertir_a_entero(valor):
    try:
        return int(valor)
    except ValueError:
        return f"Error: '{valor}' no es un número"
    except TypeError:
        return "Error: Tipo de dato no soportado"

print(f"  convertir_a_entero('123') = {convertir_a_entero('123')}")
print(f"  convertir_a_entero('abc') = {convertir_a_entero('abc')}")

print("\n" + "=" * 50)
