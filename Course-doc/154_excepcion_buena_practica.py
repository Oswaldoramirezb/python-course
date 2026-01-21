"""
EXCEPCIÓN: BUENAS PRÁCTICAS
===========================
Cómo manejar excepciones correctamente
"""

print("=" * 50)
print("BUENAS PRÁCTICAS CON EXCEPCIONES")
print("=" * 50)

print("\n1. Ser específico con los tipos de excepciones:")
print("  ✅ Bueno: except ValueError:")
print("  ❌ Malo: except: (captura todo)")

print("\n2. No silenciar errores:")
print("  ❌ Malo:")
print("     try:")
print("         operacion()")
print("     except:")
print("         pass  # Silencia todos los errores")

print("\n3. Usar finally para limpiar recursos:")
print("  ✅ Bueno:")
print("     try:")
print("         archivo = open('archivo.txt')")
print("     finally:")
print("         archivo.close()")

print("\n4. Proporcionar mensajes de error útiles:")
print("  ✅ Bueno: raise ValueError('El número debe ser positivo')")
print("  ❌ Malo: raise ValueError()")

print("\n5. Documentar excepciones que puede lanzar:")
def dividir(a, b):
    """
    Divide dos números.
    
    Raises:
        ZeroDivisionError: Si b es cero
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

print("\nEjemplo de función documentada:")
print("  dividir(10, 2) =", dividir(10, 2))

print("\n" + "=" * 50)
