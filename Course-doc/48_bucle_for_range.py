"""
BUCLE FOR: CON RANGE
====================
Usar range() para controlar las iteraciones
"""

print("=" * 50)
print("BUCLE FOR CON RANGE")
print("=" * 50)

# range(5) - del 0 al 4
print("\nrange(5) - del 0 al 4:")
for i in range(5):
    print(f"  i = {i}")

# range(2, 6) - del 2 al 5
print("\nrange(2, 6) - del 2 al 5:")
for i in range(2, 6):
    print(f"  i = {i}")

# range(0, 10, 2) - de 0 a 9, de 2 en 2
print("\nrange(0, 10, 2) - de 0 a 9, paso 2:")
for i in range(0, 10, 2):
    print(f"  i = {i}")

# range hacia atrás
print("\nrange(10, 0, -1) - contar hacia atrás:")
for i in range(10, 0, -1):
    print(f"  {i}", end=" ")
print()

print("\n" + "=" * 50)
