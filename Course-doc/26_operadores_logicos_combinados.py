"""
OPERADORES LÓGICOS: COMBINADOS
===============================
Combinar múltiples operadores lógicos
"""

print("=" * 50)
print("OPERADORES LÓGICOS COMBINADOS")
print("=" * 50)

# Combinar AND y OR
edad = 25
tiene_licencia = True
es_estudiante = False

puede_conducir = edad >= 18 and tiene_licencia
print(f"\nEjemplo 1 - AND:")
print(f"  edad = {edad}, tiene_licencia = {tiene_licencia}")
print(f"  puede_conducir = edad >= 18 and tiene_licencia")
print(f"  Resultado: {puede_conducir}")

# Combinar OR
tiene_descuento = es_estudiante or edad >= 65
print(f"\nEjemplo 2 - OR:")
print(f"  es_estudiante = {es_estudiante}, edad = {edad}")
print(f"  tiene_descuento = es_estudiante or edad >= 65")
print(f"  Resultado: {tiene_descuento}")

# Combinar AND, OR y NOT
condicion_compleja = (edad >= 18 and tiene_licencia) or es_estudiante
print(f"\nEjemplo 3 - Combinación:")
print(f"  (edad >= 18 and tiene_licencia) or es_estudiante")
print(f"  Resultado: {condicion_compleja}")

print("\n" + "=" * 50)
