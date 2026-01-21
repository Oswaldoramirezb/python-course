"""
MÉTODO ESPECIAL: __STR__
=========================
Representación legible para humanos
"""

print("=" * 50)
print("MÉTODO __STR__")
print("=" * 50)

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        """Retorna representación legible"""
        return f"'{self.titulo}' por {self.autor}"

libro = Libro("Python Básico", "Autor X")
print("\nSin __str__:")
print(f"  libro = {libro}")

print("\nCon __str__:")
print(f"  str(libro) = {str(libro)}")
print(f"  print(libro) = ", end="")
print(libro)

print("\nUso:")
print("  print(libro)  # Usa __str__")
print("  str(libro)    # Usa __str__")

print("\n" + "=" * 50)
