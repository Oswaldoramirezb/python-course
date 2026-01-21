"""
RESUMEN: MÉTODOS ESPECIALES
===========================
Todos los métodos especiales (dunder methods)
"""

print("=" * 50)
print("RESUMEN - MÉTODOS ESPECIALES")
print("=" * 50)

print("\nMétodos especiales comunes:")
print("  __init__()    - Inicializador")
print("  __str__()     - Representación legible")
print("  __repr__()    - Representación técnica")
print("  __len__()     - Longitud")
print("  __eq__()      - Igualdad (==)")
print("  __ne__()      - Desigualdad (!=)")
print("  __lt__()      - Menor que (<)")
print("  __gt__()      - Mayor que (>)")
print("  __add__()     - Suma (+)")
print("  __sub__()     - Resta (-)")
print("  __mul__()     - Multiplicación (*)")
print("  __truediv__() - División (/)")
print("  __getitem__() - Acceso con []")
print("  __setitem__() - Asignación con []")
print("  __delitem__() - Eliminación con del")
print("  __contains__() - Operador in")
print("  __call__()    - Llamar objeto como función")

print("\nEjemplo completo:")
print("  class MiClase:")
print("      def __init__(self, valor):")
print("          self.valor = valor")
print("")
print("      def __str__(self):")
print("          return f'MiClase({self.valor})'")
print("")
print("      def __add__(self, otro):")
print("          return MiClase(self.valor + otro.valor)")

print("\n" + "=" * 50)
