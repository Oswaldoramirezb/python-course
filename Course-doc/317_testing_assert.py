"""
TESTING: ASSERT
===============
Usar assert para pruebas simples
"""

print("=" * 50)
print("ASSERT - PRUEBAS SIMPLES")
print("=" * 50)

# Función a probar
def sumar(a, b):
    return a + b

# Pruebas con assert
print("\nPruebas con assert:")
print("  assert condicion, 'mensaje'")

# Pruebas básicas
assert sumar(2, 3) == 5, "Suma incorrecta"
assert sumar(0, 0) == 0, "Suma de ceros incorrecta"
assert sumar(-1, 1) == 0, "Suma de opuestos incorrecta"

print("  ✅ Todas las pruebas pasaron")

# Prueba que falla
print("\nPrueba que falla:")
try:
    assert sumar(2, 3) == 6, "Esta prueba fallará"
except AssertionError as e:
    print(f"  ❌ Error: {e}")

# Función de prueba
def test_sumar():
    """Función de prueba"""
    assert sumar(2, 3) == 5
    assert sumar(0, 0) == 0
    assert sumar(-1, 1) == 0
    print("  ✅ test_sumar() pasó")

test_sumar()

print("\nVentajas:")
print("  ✅ Simple y directo")
print("  ✅ No requiere bibliotecas")
print("  ✅ Útil para pruebas rápidas")

print("\nDesventajas:")
print("  ❌ Menos información cuando falla")
print("  ❌ No hay organización")
print("  ❌ No hay fixtures")

print("\nCuándo usar:")
print("  - Pruebas rápidas")
print("  - Validaciones simples")
print("  - Prototipos")

print("\n" + "=" * 50)
