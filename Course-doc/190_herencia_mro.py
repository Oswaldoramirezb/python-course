"""
HERENCIA: MRO (METHOD RESOLUTION ORDER)
=======================================
Orden en que Python busca métodos
"""

print("=" * 50)
print("MRO - METHOD RESOLUTION ORDER")
print("=" * 50)

class A:
    def metodo(self):
        return "Método de A"

class B(A):
    def metodo(self):
        return "Método de B"

class C(A):
    def metodo(self):
        return "Método de C"

class D(B, C):
    pass

print("\nJerarquía:")
print("     A")
print("    / \\")
print("   B   C")
print("    \\ /")
print("     D")

print("\nMRO de D:")
print(f"  D.__mro__ = {D.__mro__}")

d = D()
print(f"\n¿Qué método se ejecuta?")
print(f"  d.metodo() = {d.metodo()}")

print("\nOrden de búsqueda (MRO):")
print("  1. D (la clase misma)")
print("  2. B (primera clase padre)")
print("  3. C (segunda clase padre)")
print("  4. A (clase abuelo)")

print("\nVer MRO:")
print("  Clase.__mro__")
print("  Clase.mro()")

print("\n" + "=" * 50)
