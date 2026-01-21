"""
OPERADOR TERNARIO
=================
If-else en una sola línea
"""

print("=" * 50)
print("OPERADOR TERNARIO")
print("=" * 50)

# Sintaxis: valor_si_true if condicion else valor_si_false
edad = 20

print(f"\nedad = {edad}")

# Forma larga
if edad >= 18:
    mensaje = "Mayor de edad"
else:
    mensaje = "Menor de edad"

print(f"Forma larga: {mensaje}")

# Forma corta (ternario)
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(f"Forma corta (ternario): {mensaje}")

# Más ejemplos
numero = 7
tipo = "par" if numero % 2 == 0 else "impar"
print(f"\nnumero = {numero}")
print(f"tipo = 'par' if numero % 2 == 0 else 'impar'")
print(f"Resultado: {tipo}")

print("\n" + "=" * 50)
