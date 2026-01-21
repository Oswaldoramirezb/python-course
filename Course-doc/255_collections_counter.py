"""
COLLECTIONS: COUNTER
====================
Contar elementos de una colección
"""

print("=" * 50)
print("COUNTER")
print("=" * 50)

from collections import Counter

# Counter básico
lista = ["a", "b", "a", "c", "b", "a"]
contador = Counter(lista)

print(f"\nLista: {lista}")
print(f"Counter(lista) = {contador}")

# Acceder a conteos
print(f"\nAcceder a conteos:")
print(f"  contador['a'] = {contador['a']}")
print(f"  contador['b'] = {contador['b']}")
print(f"  contador['c'] = {contador['c']}")

# Métodos útiles
print(f"\nMétodos útiles:")
print(f"  contador.most_common(2) = {contador.most_common(2)}")
print(f"  sum(contador.values()) = {sum(contador.values())}")

# Con cadenas
texto = "programación"
contador_texto = Counter(texto)
print(f"\nCon cadena '{texto}':")
print(f"  Counter(texto) = {contador_texto}")
print(f"  contador_texto.most_common(3) = {contador_texto.most_common(3)}")

print("\n" + "=" * 50)
