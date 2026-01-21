"""
STRING: MÉTODO FORMAT
=====================
Formateo de cadenas con .format()
"""

print("=" * 50)
print("MÉTODO FORMAT()")
print("=" * 50)

# format() básico
nombre = "María"
edad = 30
print(f"\nEjemplo básico:")
mensaje = "Mi nombre es {} y tengo {} años".format(nombre, edad)
print(f"  'Mi nombre es {{}} y tengo {{}} años'.format('{nombre}', {edad})")
print(f"  Resultado: '{mensaje}'")

# format() con índices
print(f"\nCon índices:")
mensaje2 = "Hola {0}, tienes {1} años. Adiós {0}".format(nombre, edad)
print(f"  'Hola {{0}}, tienes {{1}} años. Adiós {{0}}'.format('{nombre}', {edad})")
print(f"  Resultado: '{mensaje2}'")

# format() con nombres
print(f"\nCon nombres:")
mensaje3 = "Nombre: {nombre}, Edad: {edad}".format(nombre=nombre, edad=edad)
print(f"  Resultado: '{mensaje3}'")

print("\n" + "=" * 50)
