"""
FUNCIÓN: ANY Y ALL
==================
Verificar condiciones en secuencias
"""

print("=" * 50)
print("FUNCIONES ANY() Y ALL()")
print("=" * 50)

# any() - True si AL MENOS UNO es True
lista1 = [False, False, True, False]
print(f"\nLista: {lista1}")
print(f"  any(lista1) = {any(lista1)} (hay al menos un True)")

lista2 = [False, False, False]
print(f"\nLista: {lista2}")
print(f"  any(lista2) = {any(lista2)} (todos son False)")

# all() - True si TODOS son True
lista3 = [True, True, True]
print(f"\nLista: {lista3}")
print(f"  all(lista3) = {all(lista3)} (todos son True)")

lista4 = [True, False, True]
print(f"\nLista: {lista4}")
print(f"  all(lista4) = {all(lista4)} (no todos son True)")

# Ejemplo práctico
numeros = [2, 4, 6, 8]
todos_pares = all(x % 2 == 0 for x in numeros)
print(f"\nEjemplo práctico:")
print(f"  numeros = {numeros}")
print(f"  ¿Todos son pares? {todos_pares}")

print("\n" + "=" * 50)
