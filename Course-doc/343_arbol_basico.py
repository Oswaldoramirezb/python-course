"""
ESTRUCTURAS: ÁRBOL BÁSICO
=========================
Estructura de datos jerárquica
"""

print("=" * 50)
print("ÁRBOL BÁSICO")
print("=" * 50)

# Nodo de árbol
class NodoArbol:
    """Nodo de árbol binario"""
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Árbol binario
class ArbolBinario:
    """Árbol binario simple"""
    def __init__(self, raiz):
        self.raiz = NodoArbol(raiz)
    
    def insertar(self, valor):
        """Insertar valor en el árbol"""
        self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        """Insertar recursivamente"""
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    
    def buscar(self, valor):
        """Buscar valor en el árbol"""
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        """Buscar recursivamente"""
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

print("\nÁrbol binario:")
print("  class NodoArbol:")
print("      def __init__(self, valor):")
print("          self.valor = valor")
print("          self.izquierda = None")
print("          self.derecha = None")

# Crear árbol
arbol = ArbolBinario(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)

print(f"\nInsertar: 5, 3, 7, 2, 4")
print(f"Buscar 3: {arbol.buscar(3)}")
print(f"Buscar 10: {arbol.buscar(10)}")

print("\nConceptos:")
print("  Nodo - Elemento del árbol")
print("  Raíz - Nodo superior")
print("  Hoja - Nodo sin hijos")
print("  Altura - Profundidad máxima")

print("\nRecorridos:")
print("  In-order - Izquierda, Raíz, Derecha")
print("  Pre-order - Raíz, Izquierda, Derecha")
print("  Post-order - Izquierda, Derecha, Raíz")

print("\nUsos:")
print("  ✅ Árboles de búsqueda binaria")
print("  ✅ Expresiones matemáticas")
print("  ✅ Estructuras jerárquicas")
print("  ✅ Bases de datos")

print("\n" + "=" * 50)
