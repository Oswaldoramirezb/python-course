"""
OPERADOR: DIVISIÓN ENTERA (//)
===============================
Divide números y retorna solo la parte entera (sin decimales)
"""

print("=" * 50)
print("OPERADOR DIVISIÓN ENTERA (//)")
print("=" * 50)

# División entera
a = 15
b = 4
resultado = a // b

print(f"\nDivisión entera:")
print(f"  {a} // {b} = {resultado}")
print(f"  (15 ÷ 4 = 3.75, pero // retorna solo 3)")

# Comparación con división normal
print(f"\nComparación:")
print(f"  {a} / {b} = {a / b}  (división normal)")
print(f"  {a} // {b} = {resultado}  (división entera)")

# Con flotantes también funciona
c = 15.7
d = 4.2
resultado2 = c // d
print(f"\nCon flotantes:")
print(f"  {c} // {d} = {resultado2}")

print("\n" + "=" * 50)
