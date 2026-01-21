"""
MEMORIA: REFERENCIAS
====================
Cómo funcionan las referencias
"""

print("=" * 50)
print("REFERENCIAS")
print("=" * 50)

# Referencias básicas
lista1 = [1, 2, 3]
lista2 = lista1  # lista2 referencia al mismo objeto

print("\nReferencias:")
print(f"  lista1 = {lista1}")
print(f"  lista2 = lista1  # Misma referencia")

print(f"\nVerificar misma referencia:")
print(f"  id(lista1) = {id(lista1)}")
print(f"  id(lista2) = {id(lista2)}")
print(f"  lista1 is lista2 = {lista1 is lista2}")

# Modificar afecta ambas
lista1.append(4)
print(f"\nModificar lista1:")
print(f"  lista1.append(4)")
print(f"  lista1 = {lista1}")
print(f"  lista2 = {lista2}  # También modificado")

# Copia (nueva referencia)
lista3 = lista1.copy()
print(f"\nCopia (nueva referencia):")
print(f"  lista3 = lista1.copy()")
print(f"  lista1 is lista3 = {lista1 is lista3}")
print(f"  lista3 = {lista3}")

lista3.append(5)
print(f"\nModificar lista3:")
print(f"  lista3.append(5)")
print(f"  lista1 = {lista1}  # No modificado")
print(f"  lista3 = {lista3}")

print("\n" + "=" * 50)
