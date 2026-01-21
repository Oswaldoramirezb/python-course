"""
OPERADOR: AND
==============
Ambas condiciones deben ser True para que el resultado sea True
"""

print("=" * 50)
print("OPERADOR AND")
print("=" * 50)

# AND con True y True
resultado1 = True and True
print(f"\nTrue and True = {resultado1}")

# AND con True y False
resultado2 = True and False
print(f"True and False = {resultado2}")

# Ejemplo práctico
edad = 20
tiene_licencia = True

puede_conducir = edad >= 18 and tiene_licencia

print(f"\nEjemplo práctico:")
print(f"  edad = {edad}")
print(f"  tiene_licencia = {tiene_licencia}")
print(f"  puede_conducir = edad >= 18 and tiene_licencia")
print(f"  Resultado: {puede_conducir}")

print("\n" + "=" * 50)
