"""
OPERADOR: TERNARIO
==================
Expresión condicional en una línea
"""

print("=" * 50)
print("OPERADOR TERNARIO")
print("=" * 50)

# Operador ternario básico
edad = 20
estado = "Mayor" if edad >= 18 else "Menor"
print(f"\nOperador ternario básico:")
print(f"  edad = {edad}")
print(f"  estado = 'Mayor' if edad >= 18 else 'Menor'")
print(f"  estado = {estado}")

# Comparación con if-else
print("\nComparación:")
print("  Con if-else:")
print("    if edad >= 18:")
print("        estado = 'Mayor'")
print("    else:")
print("        estado = 'Menor'")
print("")
print("  Con ternario:")
print("    estado = 'Mayor' if edad >= 18 else 'Menor'")

# Múltiples condiciones
print("\nMúltiples condiciones:")
nota = 85
calificacion = "A" if nota >= 90 else "B" if nota >= 80 else "C" if nota >= 70 else "F"
print(f"  nota = {nota}")
print(f"  calificacion = {calificacion}")

# En expresiones
print("\nEn expresiones:")
a, b = 10, 5
maximo = a if a > b else b
print(f"  a = {a}, b = {b}")
print(f"  maximo = a if a > b else b = {maximo}")

# Con funciones
print("\nCon funciones:")
def es_par(n):
    return "Par" if n % 2 == 0 else "Impar"

print(f"  es_par(4) = {es_par(4)}")
print(f"  es_par(5) = {es_par(5)}")

# En list comprehension
print("\nEn list comprehension:")
numeros = [1, 2, 3, 4, 5, 6]
resultado = ["Par" if x % 2 == 0 else "Impar" for x in numeros]
print(f"  numeros = {numeros}")
print(f"  resultado = {resultado}")

# Asignación condicional
print("\nAsignación condicional:")
valor = None
valor_final = valor if valor is not None else "Valor por defecto"
print(f"  valor_final = {valor_final}")

print("\nSintaxis:")
print("  valor_si_verdadero if condicion else valor_si_falso")

print("\nVentajas:")
print("  ✅ Código más compacto")
print("  ✅ Legible para condiciones simples")
print("  ✅ Útil en expresiones")

print("\nCuándo usar:")
print("  ✅ Condiciones simples")
print("  ✅ Asignaciones condicionales")
print("  ❌ Evitar para lógica compleja")

print("\n" + "=" * 50)
