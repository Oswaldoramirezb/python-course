"""
MÉTODO ESPECIAL: __SETITEM__
============================
Asignar valores con []
"""

print("=" * 50)
print("MÉTODO __SETITEM__")
print("=" * 50)

class MiLista:
    def __init__(self, elementos):
        self.elementos = list(elementos)
    
    def __getitem__(self, indice):
        return self.elementos[indice]
    
    def __setitem__(self, indice, valor):
        """Permite usar objeto[indice] = valor"""
        self.elementos[indice] = valor
    
    def __str__(self):
        return str(self.elementos)

mi_lista = MiLista([1, 2, 3, 4, 5])
print("\nCon __setitem__:")
print(f"  mi_lista = {mi_lista}")

mi_lista[0] = 10
print(f"  mi_lista[0] = 10 → {mi_lista}")

mi_lista[2] = 30
print(f"  mi_lista[2] = 30 → {mi_lista}")

# Con diccionario personalizado
class MiDiccionario:
    def __init__(self):
        self.datos = {}
    
    def __getitem__(self, clave):
        return self.datos.get(clave)
    
    def __setitem__(self, clave, valor):
        self.datos[clave] = valor

mi_dict = MiDiccionario()
mi_dict["nombre"] = "Juan"
mi_dict["edad"] = 30
print(f"\nCon diccionario:")
print(f"  mi_dict['nombre'] = {mi_dict['nombre']}")
print(f"  mi_dict['edad'] = {mi_dict['edad']}")

print("\n" + "=" * 50)
