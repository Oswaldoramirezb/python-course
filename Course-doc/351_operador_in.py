"""
OPERADOR: IN
============
Verificar si elemento está en secuencia
"""

print("=" * 50)
print("OPERADOR IN")
print("=" * 50)

# Con listas
lista = [1, 2, 3, 4, 5]
print(f"\nLista: {lista}")

print(f"\nVerificar elementos:")
print(f"  2 in lista = {2 in lista}")
print(f"  10 in lista = {10 in lista}")
print(f"  2 not in lista = {2 not in lista}")

# Con cadenas
texto = "Python"
print(f"\nCadena: '{texto}'")
print(f"  'P' in texto = {'P' in texto}")
print(f"  'py' in texto = {'py' in texto}")  # Case sensitive
print(f"  'thon' in texto = {'thon' in texto}")

# Con diccionarios (claves)
diccionario = {"nombre": "Juan", "edad": 30}
print(f"\nDiccionario: {diccionario}")
print(f"  'nombre' in diccionario = {'nombre' in diccionario}")
print(f"  'Juan' in diccionario = {'Juan' in diccionario}")  # Solo claves

# Con sets
conjunto = {1, 2, 3, 4, 5}
print(f"\nSet: {conjunto}")
print(f"  3 in conjunto = {3 in conjunto}")
print(f"  10 in conjunto = {10 in conjunto}")

# Con tuplas
tupla = (1, 2, 3)
print(f"\nTupla: {tupla}")
print(f"  2 in tupla = {2 in tupla}")

# En condicionales
print("\nEn condicionales:")
if 3 in lista:
    print("  ✅ 3 está en la lista")

# Con not in
print("\nOperador not in:")
print(f"  10 not in lista = {10 not in lista}")

print("\nComplejidad:")
print("  Lista/Tupla: O(n) - Lineal")
print("  Set/Dict: O(1) - Constante (promedio)")

print("\n" + "=" * 50)
