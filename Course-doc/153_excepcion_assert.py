"""
EXCEPCIÓN: ASSERT
=================
Afirmaciones para validar condiciones
"""

print("=" * 50)
print("ASSERT - AFIRMACIONES")
print("=" * 50)

# assert básico
print("\nEjemplo 1 - assert básico:")
def calcular_promedio(notas):
    assert len(notas) > 0, "La lista de notas no puede estar vacía"
    assert all(0 <= nota <= 100 for nota in notas), "Las notas deben estar entre 0 y 100"
    return sum(notas) / len(notas)

try:
    promedio = calcular_promedio([85, 90, 78])
    print(f"  ✅ Promedio: {promedio}")
except AssertionError as e:
    print(f"  ❌ Error de aserción: {e}")

# assert con condición falsa
print("\nEjemplo 2 - assert que falla:")
try:
    assert 5 > 10, "5 no es mayor que 10"
except AssertionError as e:
    print(f"  ✅ AssertionError capturado: {e}")

# assert para debugging
print("\nEjemplo 3 - assert para debugging:")
def dividir(a, b):
    assert b != 0, "El divisor no puede ser cero"
    return a / b

try:
    resultado = dividir(10, 0)
except AssertionError as e:
    print(f"  ✅ Error de aserción: {e}")

print("\n⚠️  NOTA: assert se puede deshabilitar con -O al ejecutar Python")

print("\n" + "=" * 50)
