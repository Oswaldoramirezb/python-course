"""
OPERADOR: MÓDULO (%)
====================
Da el RESTO de una división
"""

print("=" * 50)
print("OPERADOR MÓDULO (%)")
print("=" * 50)

# Ejemplo: 15 dividido entre 4
# 15 ÷ 4 = 3 con resto 3
a = 15
b = 4
resto = a % b

print(f"\nMódulo (resto de división):")
print(f"  {a} % {b} = {resto}")
print(f"  (porque 15 ÷ 4 = 3 con resto {resto})")

# Verificar si es par o impar
numero = 7
es_par = numero % 2 == 0

print(f"\n¿{numero} es par?")
print(f"  {numero} % 2 = {numero % 2}")
print(f"  ¿Es 0? {es_par}")
print(f"  Respuesta: {'Sí' if es_par else 'No, es impar'}")

print("\n" + "=" * 50)
