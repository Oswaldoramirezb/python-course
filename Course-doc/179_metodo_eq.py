"""
MÉTODO ESPECIAL: __EQ__
========================
Definir igualdad entre objetos
"""

print("=" * 50)
print("MÉTODO __EQ__")
print("=" * 50)

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __eq__(self, otro):
        """Define cuándo dos libros son iguales"""
        if isinstance(otro, Libro):
            return self.titulo == otro.titulo and self.autor == otro.autor
        return False

libro1 = Libro("Python", "Autor X")
libro2 = Libro("Python", "Autor X")
libro3 = Libro("Java", "Autor Y")

print("\nComparar objetos:")
print(f"  libro1 = Libro('Python', 'Autor X')")
print(f"  libro2 = Libro('Python', 'Autor X')")
print(f"  libro3 = Libro('Java', 'Autor Y')")

print(f"\n  libro1 == libro2 = {libro1 == libro2}")
print(f"  libro1 == libro3 = {libro1 == libro3}")

print("\nSin __eq__, compara identidad (is):")
print("  libro1 == libro2 → False (objetos diferentes)")

print("\nCon __eq__, compara valores:")
print("  libro1 == libro2 → True (mismos valores)")

print("\n" + "=" * 50)
