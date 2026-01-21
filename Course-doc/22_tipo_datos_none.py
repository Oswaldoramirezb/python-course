"""
TIPO DE DATO: NONE
==================
None significa "nada" o "vacío"
"""

print("=" * 50)
print("NONE - Valor Nulo")
print("=" * 50)

# None es un valor especial
valor = None

print(f"\nvalor = {valor}")
print(f"Tipo: {type(valor).__name__}")

# Uso común: cuando algo no existe
def buscar_elemento(lista, elemento):
    """Retorna el índice o None si no existe"""
    if elemento in lista:
        return lista.index(elemento)
    return None

print("\nEjemplo práctico:")
lista = [1, 2, 3]
resultado = buscar_elemento(lista, 5)
print(f"  Buscar 5 en {lista}: {resultado}")

# Comparar con None
print(f"\nComparar con None:")
print(f"  valor is None: {valor is None}")
print(f"  valor == None: {valor == None} (funciona pero usar 'is' es mejor)")

print("\n" + "=" * 50)
