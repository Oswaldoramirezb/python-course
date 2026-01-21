"""
BUCLE WHILE: CON CONDICIÓN
==========================
Controlar el bucle con una condición
"""

print("=" * 50)
print("BUCLE WHILE CON CONDICIÓN")
print("=" * 50)

# While con condición compleja
print("\nEjemplo 1 - Sumar hasta llegar a 100:")
suma = 0
numero = 1
while suma < 100:
    suma += numero
    print(f"  Sumando {numero}, total: {suma}")
    numero += 1

# While con múltiples condiciones
print("\nEjemplo 2 - Múltiples condiciones:")
edad = 0
while edad < 18 and edad >= 0:
    print(f"  Edad: {edad} (menor de edad)")
    edad += 5  # Simulación

print("\n" + "=" * 50)
