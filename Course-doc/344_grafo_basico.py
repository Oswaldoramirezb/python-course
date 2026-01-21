"""
ESTRUCTURAS: GRAFO BÁSICO
=========================
Nodos y aristas
"""

print("=" * 50)
print("GRAFO BÁSICO")
print("=" * 50)

# Grafo con lista de adyacencia
class Grafo:
    """Grafo implementado con lista de adyacencia"""
    def __init__(self):
        self.adyacencia = {}
    
    def agregar_nodo(self, nodo):
        """Agregar nodo al grafo"""
        if nodo not in self.adyacencia:
            self.adyacencia[nodo] = []
    
    def agregar_arista(self, origen, destino):
        """Agregar arista entre nodos"""
        if origen not in self.adyacencia:
            self.agregar_nodo(origen)
        if destino not in self.adyacencia:
            self.agregar_nodo(destino)
        
        self.adyacencia[origen].append(destino)
        # Para grafo no dirigido, descomentar:
        # self.adyacencia[destino].append(origen)
    
    def obtener_vecinos(self, nodo):
        """Obtener nodos adyacentes"""
        return self.adyacencia.get(nodo, [])
    
    def mostrar(self):
        """Mostrar grafo"""
        for nodo, vecinos in self.adyacencia.items():
            print(f"  {nodo} -> {vecinos}")

print("\nGrafo:")
print("  class Grafo:")
print("      def __init__(self):")
print("          self.adyacencia = {}")

# Crear grafo
grafo = Grafo()
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'D')

print("\nGrafo creado:")
grafo.mostrar()

print(f"\nVecinos de A: {grafo.obtener_vecinos('A')}")
print(f"Vecinos de B: {grafo.obtener_vecinos('B')}")

print("\nConceptos:")
print("  Nodo/Vértice - Punto en el grafo")
print("  Arista/Edge - Conexión entre nodos")
print("  Dirigido - Dirección definida")
print("  No dirigido - Sin dirección")

print("\nRepresentaciones:")
print("  Lista de adyacencia - Diccionario de listas")
print("  Matriz de adyacencia - Matriz 2D")

print("\nAlgoritmos:")
print("  BFS - Breadth-First Search")
print("  DFS - Depth-First Search")
print("  Dijkstra - Camino más corto")

print("\nUsos:")
print("  ✅ Redes sociales")
print("  ✅ Mapas y navegación")
print("  ✅ Redes de computadoras")
print("  ✅ Dependencias")

print("\n" + "=" * 50)
