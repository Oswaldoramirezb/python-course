"""
CONDICIONAL: IF SIMPLE
======================
Si la condición es True, ejecuta el código
"""

print("=" * 50)
print("IF SIMPLE")
print("=" * 50)

edad = 20
print(f"\nedad = {edad}")

if edad >= 18:
    print("  ✅ Eres mayor de edad")

print("\n--- Si edad es menor ---")
edad = 16
print(f"edad = {edad}")

if edad >= 18:
    print("  ✅ Eres mayor de edad")
else:
    print("  ❌ Eres menor de edad")

print("\n" + "=" * 50)
