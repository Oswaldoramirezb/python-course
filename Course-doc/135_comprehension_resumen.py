"""
RESUMEN: COMPREHENSIONS
=======================
Todas las comprehensions en Python
"""

print("=" * 50)
print("RESUMEN - COMPREHENSIONS")
print("=" * 50)

print("\nList Comprehension:")
print("  [expresión for item in iterable]")
print("  [x**2 for x in range(5)]")

print("\nDict Comprehension:")
print("  {clave: valor for item in iterable}")
print("  {x: x**2 for x in range(5)}")

print("\nSet Comprehension:")
print("  {expresión for item in iterable}")
print("  {x**2 for x in range(5)}")

print("\nCon condición (filtro):")
print("  [x for x in range(10) if x % 2 == 0]")

print("\nCon if-else (transformación):")
print("  [x if x%2==0 else -x for x in range(10)]")

print("\nMúltiples condiciones:")
print("  [x for x in range(20) if x%2==0 if x>10]")

print("\nAnidadas:")
print("  [[x*y for y in range(3)] for x in range(3)]")

print("\n" + "=" * 50)
