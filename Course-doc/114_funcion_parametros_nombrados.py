"""
FUNCIÓN: PARÁMETROS NOMBRADOS
=============================
Pasar argumentos por nombre (keyword arguments)
"""

print("=" * 50)
print("PARÁMETROS NOMBRADOS")
print("=" * 50)

# Función con múltiples parámetros
def presentar(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, de {ciudad}"

print("\nLlamada por posición:")
print(f"  presentar('María', 25, 'Barcelona')")
print(f"    = {presentar('María', 25, 'Barcelona')}")

print("\nLlamada por nombre:")
print(f"  presentar(ciudad='Madrid', nombre='Pedro', edad=30)")
print(f"    = {presentar(ciudad='Madrid', nombre='Pedro', edad=30)}")

print("\nCombinación:")
print(f"  presentar('Ana', edad=28, ciudad='Valencia')")
print(f"    = {presentar('Ana', edad=28, ciudad='Valencia')}")

print("\n" + "=" * 50)
