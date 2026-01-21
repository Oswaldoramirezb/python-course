"""
STRING: MÉTODO FIND
===================
Busca un texto y retorna su posición
"""

print("=" * 50)
print("MÉTODO FIND()")
print("=" * 50)

# find() - buscar texto
texto = "Python es genial"
print(f"\nTexto: '{texto}'")

posicion = texto.find("genial")
print(f"find('genial') = {posicion}")

# find() - si no encuentra, retorna -1
posicion2 = texto.find("Java")
print(f"find('Java') = {posicion2} (no encontrado)")

# find() con inicio
texto2 = "hola hola mundo"
print(f"\nCon inicio de búsqueda:")
print(f"  '{texto2}'")
posicion3 = texto2.find("hola", 5)
print(f"  find('hola', 5) = {posicion3}")

print("\n" + "=" * 50)
