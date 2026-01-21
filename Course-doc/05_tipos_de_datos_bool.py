"""
TIPO DE DATO: BOOL (BOOLEANOS)
===============================
Solo hay dos valores: True (verdadero) o False (falso)
"""

print("=" * 50)
print("BOOLEANOS (bool)")
print("=" * 50)

# Crear variables booleanas
es_verdadero = True
es_falso = False

print(f"\nVerdadero: {es_verdadero}")
print(f"Falso: {es_falso}")

# Ver el tipo
print(f"\nEl tipo de {es_verdadero} es: {type(es_verdadero).__name__}")

# Ejemplo práctico
es_mayor = 10 > 5
print(f"\n¿10 es mayor que 5? {es_mayor}")

es_menor = 3 < 2
print(f"¿3 es menor que 2? {es_menor}")

print("\n" + "=" * 50)
