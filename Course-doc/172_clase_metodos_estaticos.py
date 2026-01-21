"""
CLASE: MÉTODOS ESTÁTICOS
========================
Métodos que no necesitan instancia ni clase
"""

print("=" * 50)
print("MÉTODOS ESTÁTICOS")
print("=" * 50)

class Utilidades:
    @staticmethod
    def sumar(a, b):
        """Método estático: no necesita self ni cls"""
        return a + b
    
    @staticmethod
    def es_par(numero):
        """Método estático: puede llamarse sin crear objeto"""
        return numero % 2 == 0

print("\nMétodos estáticos:")
print("  @staticmethod")
print("  def metodo():")
print("      pass")

print("\nLlamar método estático:")
print(f"  Utilidades.sumar(5, 3) = {Utilidades.sumar(5, 3)}")
print(f"  Utilidades.es_par(10) = {Utilidades.es_par(10)}")

# También desde instancia
util = Utilidades()
print(f"\nDesde instancia también funciona:")
print(f"  util.sumar(10, 20) = {util.sumar(10, 20)}")

print("\nVentajas:")
print("  ✅ No necesita crear objeto")
print("  ✅ Organización lógica")
print("  ✅ No accede a self ni cls")

print("\n" + "=" * 50)
