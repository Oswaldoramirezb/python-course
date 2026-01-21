"""
CONDICIONAL: IF-ELSE
====================
Si la condición es True, ejecuta el bloque if
Si es False, ejecuta el bloque else
"""

print("=" * 50)
print("IF-ELSE")
print("=" * 50)

temperatura = 25
print(f"\ntemperatura = {temperatura}°C")

if temperatura > 30:
    print("  🔥 Hace mucho calor")
else:
    print("  😊 La temperatura está bien")

print("\n--- Cambiando temperatura ---")
temperatura = 35
print(f"temperatura = {temperatura}°C")

if temperatura > 30:
    print("  🔥 Hace mucho calor")
else:
    print("  😊 La temperatura está bien")

print("\n" + "=" * 50)
