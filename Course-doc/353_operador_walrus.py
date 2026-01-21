"""
OPERADOR: WALRUS (:=)
=====================
Asignación en expresiones (Python 3.8+)
"""

print("=" * 50)
print("OPERADOR WALRUS (:=)")
print("=" * 50)

# Walrus operator básico
print("\nWalrus operator (:=):")
print("  Permite asignar y usar en la misma expresión")

# Ejemplo 1: En while
print("\n1. En bucle while:")
print("  while (line := input()) != 'quit':")
print("      print(line)")

# Ejemplo 2: En if
print("\n2. En condicional if:")
lista = [1, 2, 3, 4, 5]
if (n := len(lista)) > 3:
    print(f"  Lista tiene {n} elementos (más de 3)")

# Ejemplo 3: En list comprehension
print("\n3. En list comprehension:")
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = [cuadrado for x in datos if (cuadrado := x**2) > 20]
print(f"  Cuadrados mayores a 20: {cuadrados}")

# Ejemplo 4: En expresiones
print("\n4. En expresiones:")
texto = "Python es genial"
if (palabras := texto.split()):
    print(f"  Número de palabras: {len(palabras)}")
    print(f"  Palabras: {palabras}")

# Comparación: con y sin walrus
print("\nComparación:")
print("  Sin walrus:")
print("    resultado = funcion()")
print("    if resultado:")
print("        usar(resultado)")
print("")
print("  Con walrus:")
print("    if (resultado := funcion()):")
print("        usar(resultado)")

# Ejemplo práctico: procesar archivo
print("\nEjemplo práctico - Procesar líneas:")
lineas = ["línea1", "línea2", "línea3", ""]
while (linea := lineas.pop(0) if lineas else ""):
    if linea:
        print(f"  Procesando: {linea}")

print("\nVentajas:")
print("  ✅ Menos código")
print("  ✅ Más legible en algunos casos")
print("  ✅ Evita asignaciones separadas")

print("\n⚠️  IMPORTANTE:")
print("  - Python 3.8+")
print("  - Usar con moderación")
print("  - No abusar, puede reducir legibilidad")

print("\n" + "=" * 50)
