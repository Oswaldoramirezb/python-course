"""
COLLECTIONS: USO PRÁCTICO
==========================
Ejemplos prácticos de collections
"""

print("=" * 50)
print("USO PRÁCTICO DE COLLECTIONS")
print("=" * 50)

from collections import Counter, defaultdict, deque

# Counter - Contar palabras
texto = "python es genial python es fácil python es poderoso"
palabras = texto.split()
contador = Counter(palabras)

print("\nCounter - Contar palabras:")
print(f"  texto = '{texto}'")
print(f"  Palabra más común: {contador.most_common(1)}")

# defaultdict - Agrupar por categoría
productos = [
    ("fruta", "manzana"),
    ("fruta", "banana"),
    ("verdura", "zanahoria"),
    ("fruta", "naranja")
]

grupos = defaultdict(list)
for categoria, producto in productos:
    grupos[categoria].append(producto)

print("\ndefaultdict - Agrupar:")
print(f"  grupos = {dict(grupos)}")

# deque - Cola FIFO
cola = deque()
cola.append("primero")
cola.append("segundo")
cola.append("tercero")

print("\ndeque - Cola:")
print(f"  Cola: {list(cola)}")
print(f"  Procesar: {cola.popleft()}")
print(f"  Cola restante: {list(cola)}")

print("\n" + "=" * 50)
