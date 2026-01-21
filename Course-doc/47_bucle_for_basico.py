"""
BUCLE FOR: BÁSICO
=================
Repetir código un número determinado de veces
"""

print("=" * 50)
print("BUCLE FOR BÁSICO")
print("=" * 50)

# For básico con range
print("\nEjemplo 1 - Contar del 0 al 4:")
for i in range(5):
    print(f"  Iteración {i}: i = {i}")

# For con lista
print("\nEjemplo 2 - Iterar sobre lista:")
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"  Fruta: {fruta}")

# For con cadena
print("\nEjemplo 3 - Iterar sobre cadena:")
texto = "Python"
for letra in texto:
    print(f"  Letra: {letra}")

print("\n" + "=" * 50)
