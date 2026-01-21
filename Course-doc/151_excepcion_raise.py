"""
EXCEPCIÓN: RAISE
================
Levantar (lanzar) excepciones manualmente
"""

print("=" * 50)
print("RAISE - LEVANTAR EXCEPCIONES")
print("=" * 50)

# raise básico
print("\nEjemplo 1 - raise básico:")
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 150:
        raise ValueError("La edad no puede ser mayor a 150")
    return True

try:
    validar_edad(-5)
except ValueError as e:
    print(f"  ✅ Error capturado: {e}")

# raise con tipo específico
print("\nEjemplo 2 - raise con tipo específico:")
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

try:
    resultado = dividir(10, 0)
except ZeroDivisionError as e:
    print(f"  ✅ Error capturado: {e}")

# Re-raise (volver a lanzar)
print("\nEjemplo 3 - Re-raise:")
def procesar(numero):
    try:
        if numero < 0:
            raise ValueError("Número negativo")
    except ValueError:
        print("  Error en procesar, re-lanzando...")
        raise  # Vuelve a lanzar la excepción

try:
    procesar(-5)
except ValueError as e:
    print(f"  ✅ Error capturado en nivel superior: {e}")

print("\n" + "=" * 50)
