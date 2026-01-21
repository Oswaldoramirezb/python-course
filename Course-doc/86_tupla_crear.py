"""
TUPLA: CREAR
============
Crear tuplas en Python
"""

print("=" * 50)
print("CREAR TUPLAS")
print("=" * 50)

# Crear tupla vacía
tupla_vacia = ()
print(f"\nTupla vacía: {tupla_vacia}")

# Crear tupla con elementos
tupla1 = (1, 2, 3, 4, 5)
print(f"Tupla de números: {tupla1}")

tupla2 = ("a", "b", "c")
print(f"Tupla de cadenas: {tupla2}")

tupla3 = (1, "dos", 3.0, True)
print(f"Tupla mixta: {tupla3}")

# ⚠️ Tupla de un elemento necesita coma
tupla_un_elemento = (5,)
print(f"Tupla un elemento: {tupla_un_elemento}")

# Sin paréntesis también funciona
tupla4 = 1, 2, 3
print(f"Sin paréntesis: {tupla4}")

print("\n" + "=" * 50)
