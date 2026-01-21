"""
HASH: FUNCIÓN
=============
Usar la función hash()
"""

print("=" * 50)
print("FUNCIÓN HASH()")
print("=" * 50)

# hash() con diferentes tipos
print("\nHash de diferentes tipos:")

# Enteros
numero = 42
print(f"  hash({numero}) = {hash(numero)}")

# Cadenas
texto = "Python"
print(f"  hash('{texto}') = {hash(texto)}")

# Tuplas (inmutables)
tupla = (1, 2, 3)
print(f"  hash({tupla}) = {hash(tupla)}")

# Mismo valor, mismo hash
texto2 = "Python"
print(f"\nMismo valor, mismo hash:")
print(f"  hash('{texto}') = {hash(texto)}")
print(f"  hash('{texto2}') = {hash(texto2)}")
print(f"  Son iguales: {hash(texto) == hash(texto2)}")

# Diferentes valores, diferentes hashes
print(f"\nDiferentes valores:")
print(f"  hash('Python') = {hash('Python')}")
print(f"  hash('Java') = {hash('Java')}")

print("\n⚠️  IMPORTANTE:")
print("  - Hash puede cambiar entre ejecuciones")
print("  - No usar hash para persistencia")
print("  - Usar solo para estructuras de datos en memoria")

print("\n" + "=" * 50)
