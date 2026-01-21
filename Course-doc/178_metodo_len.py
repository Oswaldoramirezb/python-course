"""
MÉTODO ESPECIAL: __LEN__
=========================
Definir la longitud de un objeto
"""

print("=" * 50)
print("MÉTODO __LEN__")
print("=" * 50)

class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos
    
    def __len__(self):
        """Retorna la longitud del objeto"""
        return len(self.elementos)

mi_lista = MiLista([1, 2, 3, 4, 5])
print("\nCon __len__:")
print(f"  mi_lista = MiLista([1, 2, 3, 4, 5])")
print(f"  len(mi_lista) = {len(mi_lista)}")

# Ejemplo con colección
class Coleccion:
    def __init__(self):
        self.items = []
    
    def agregar(self, item):
        self.items.append(item)
    
    def __len__(self):
        return len(self.items)

coleccion = Coleccion()
coleccion.agregar("item1")
coleccion.agregar("item2")
print(f"\nColección:")
print(f"  len(coleccion) = {len(coleccion)}")

print("\n" + "=" * 50)
