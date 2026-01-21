"""
EXCEPCIÓN: FINALLY
==================
Código que SIEMPRE se ejecuta
"""

print("=" * 50)
print("TRY-EXCEPT-FINALLY")
print("=" * 50)

# try-except-finally
print("\nEjemplo 1 - finally siempre se ejecuta:")
try:
    resultado = 10 / 2
    print(f"  Resultado: {resultado}")
except ZeroDivisionError:
    print("  ❌ Error: División por cero")
finally:
    print("  ✅ Finally: Este código siempre se ejecuta")

# Con error
print("\nEjemplo 2 - finally incluso con error:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("  ❌ Error capturado")
finally:
    print("  ✅ Finally: Se ejecuta incluso con error")

# Útil para limpiar recursos
print("\nEjemplo 3 - Limpiar recursos:")
archivo = None
try:
    archivo = open("ejemplo.txt", "r", encoding="utf-8")
    contenido = archivo.read()
    print("  ✅ Archivo leído")
except FileNotFoundError:
    print("  ❌ Archivo no encontrado")
finally:
    if archivo:
        archivo.close()
        print("  ✅ Archivo cerrado (siempre)")

print("\n" + "=" * 50)
