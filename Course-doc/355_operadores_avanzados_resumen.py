"""
RESUMEN: OPERADORES AVANZADOS
=============================
Todos los operadores avanzados
"""

print("=" * 50)
print("RESUMEN - OPERADORES AVANZADOS")
print("=" * 50)

print("\nOperador in:")
print("  elemento in secuencia")
print("  elemento not in secuencia")
print("  - Verifica si elemento está en secuencia")
print("  - Listas, tuplas, sets, diccionarios, cadenas")

print("\nOperador is:")
print("  objeto1 is objeto2")
print("  objeto1 is not objeto2")
print("  - Compara identidad (mismo objeto)")
print("  - Diferente de == (que compara valores)")
print("  - Útil para: if valor is None")

print("\nOperador walrus (:=):")
print("  (variable := expresion)")
print("  - Asigna y usa en la misma expresión")
print("  - Python 3.8+")
print("  - Ejemplo: if (resultado := funcion()):")

print("\nOperador ternario:")
print("  valor_si_verdadero if condicion else valor_si_falso")
print("  - Expresión condicional en una línea")
print("  - Ejemplo: maximo = a if a > b else b")

print("\nComparación:")
print("  in - Pertenencia")
print("  is - Identidad")
print("  := - Asignación en expresión")
print("  if-else - Condicional ternario")

print("\nComplejidad:")
print("  in - O(n) en listas, O(1) en sets/dicts")
print("  is - O(1) - Comparación de identidad")
print("  := - O(1) - Asignación")
print("  ternario - O(1) - Evaluación condicional")

print("\nUsos comunes:")
print("  ✅ in - Verificar pertenencia")
print("  ✅ is - Comparar con None")
print("  ✅ := - Simplificar código")
print("  ✅ ternario - Asignaciones condicionales")

print("\n" + "=" * 50)
