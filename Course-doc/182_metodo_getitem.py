"""
MÉTODO ESPECIAL: __GETITEM__
============================
Acceder a elementos con []
"""

print("=" * 50)
print("MÉTODO __GETITEM__")
print("=" * 50)

class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos
    
    def __getitem__(self, indice):
        """Permite usar objeto[indice]"""
        return self.elementos[indice]

mi_lista = MiLista([10, 20, 30, 40, 50])
print("\nCon __getitem__:")
print(f"  mi_lista = MiLista([10, 20, 30, 40, 50])")
print(f"  mi_lista[0] = {mi_lista[0]}")
print(f"  mi_lista[2] = {mi_lista[2]}")
print(f"  mi_lista[-1] = {mi_lista[-1]}")

# Con diccionario personalizado
class MiDiccionario:
    def __init__(self):
        self.datos = {}
    
    def __getitem__(self, clave):
        return self.datos.get(clave, "No encontrado")
    
    def __setitem__(self, clave, valor):
        self.datos[clave] = valor

mi_dict = MiDiccionario()
mi_dict["nombre"] = "Juan"
print(f"\nCon diccionario personalizado:")
print(f"  mi_dict['nombre'] = {mi_dict['nombre']}")

print("\n" + "=" * 50)
