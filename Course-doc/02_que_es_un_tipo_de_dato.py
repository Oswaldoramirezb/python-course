"""
¿QUÉ ES UN TIPO DE DATO?
========================
Cada dato en Python tiene un tipo que define qué es y qué puede hacer
"""

print("=" * 50)
print("TIPOS DE DATOS - Concepto")
print("=" * 50)

print("\nUn tipo de dato define:")
print("  - Qué clase de información es")
print("  - Qué operaciones puedes hacer con ella")
print("  - Cómo se almacena en memoria")

print("\nTipos básicos en Python:")
print("  int    - Números enteros: 1, 2, -5, 0")
print("  float  - Números decimales: 3.14, 2.5, -0.5")
print("  str    - Texto: 'Hola', 'Mundo'")
print("  bool   - Verdadero o Falso: True, False")
print("  None   - Nada/vacío: None")

print("\nEjemplo:")
numero = 5
texto = "Hola"

print(f"  numero = {numero}")
print(f"  Tipo de numero: {type(numero).__name__}")

print(f"\n  texto = '{texto}'")
print(f"  Tipo de texto: {type(texto).__name__}")

print("\n" + "=" * 50)
