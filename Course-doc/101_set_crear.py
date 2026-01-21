"""
SET: CREAR
==========
Crear sets (conjuntos) en Python
"""

print("=" * 50)
print("CREAR SETS")
print("=" * 50)

# Crear set vacío
set_vacio = set()  # ⚠️ No usar {} (eso es diccionario)
print(f"\nSet vacío: {set_vacio}")

# Crear set con elementos
set1 = {1, 2, 3, 4, 5}
print(f"Set de números: {set1}")

set2 = {"manzana", "banana", "naranja"}
print(f"Set de cadenas: {set2}")

# Crear desde lista
lista = [1, 2, 2, 3, 3, 3]
set3 = set(lista)
print(f"Desde lista {lista}: {set3} (elimina duplicados)")

# ⚠️ Los sets no permiten duplicados
set4 = {1, 2, 2, 3, 3, 3}
print(f"Con duplicados: {set4} (automáticamente eliminados)")

print("\n" + "=" * 50)
