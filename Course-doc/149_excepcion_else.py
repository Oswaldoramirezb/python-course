"""
EXCEPCIÓN: ELSE
===============
Ejecutar código cuando NO hay excepción
"""

print("=" * 50)
print("TRY-EXCEPT-ELSE")
print("=" * 50)

# try-except-else
print("\nEjemplo 1 - else cuando no hay error:")
try:
    numero = int("123")
except ValueError:
    print("  ❌ Error: No es un número válido")
else:
    print(f"  ✅ Conversión exitosa: {numero}")

# Comparación
print("\nEjemplo 2 - Comparación:")
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("  ❌ Error: División por cero")
else:
    print(f"  ✅ División exitosa: {resultado}")
    print("  (Este código solo se ejecuta si NO hay error)")

# Útil para validación
print("\nEjemplo 3 - Validación:")
def procesar_numero(texto):
    try:
        numero = int(texto)
    except ValueError:
        return None
    else:
        return numero * 2

print(f"  procesar_numero('5') = {procesar_numero('5')}")
print(f"  procesar_numero('abc') = {procesar_numero('abc')}")

print("\n" + "=" * 50)
