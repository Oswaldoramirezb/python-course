"""
MÉTODO ESPECIAL: __REPR__
==========================
Representación técnica para desarrolladores
"""

print("=" * 50)
print("MÉTODO __REPR__")
print("=" * 50)

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        """Para usuarios finales"""
        return f"'{self.titulo}' por {self.autor}"
    
    def __repr__(self):
        """Para desarrolladores (debe ser código Python válido)"""
        return f"Libro('{self.titulo}', '{self.autor}', {self.paginas})"

libro = Libro("Python Básico", "Autor X", 300)
print("\nDiferencia entre __str__ y __repr__:")
print(f"  str(libro) = {str(libro)}")
print(f"  repr(libro) = {repr(libro)}")

print("\nUso:")
print("  print(libro)     # Usa __str__")
print("  repr(libro)      # Usa __repr__")
print("  [libro]          # Usa __repr__ en listas")

print("\n" + "=" * 50)
