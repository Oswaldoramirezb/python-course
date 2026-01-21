"""
RESUMEN: ENCAPSULACIÓN
=====================
Todas las operaciones con encapsulación
"""

print("=" * 50)
print("RESUMEN - ENCAPSULACIÓN")
print("=" * 50)

print("\nNiveles de acceso:")
print("  Público:    atributo (sin prefijo)")
print("  Protegido:  _atributo (un guion bajo)")
print("  Privado:    __atributo (dos guiones bajos)")

print("\nGetter y Setter:")
print("  def get_atributo(self):")
print("      return self._atributo")
print("")
print("  def set_atributo(self, valor):")
print("      self._atributo = valor")

print("\nCon @property (recomendado):")
print("  @property")
print("  def atributo(self):")
print("      return self._atributo")
print("")
print("  @atributo.setter")
print("  def atributo(self, valor):")
print("      self._atributo = valor")

print("\nVentajas:")
print("  ✅ Protección de datos")
print("  ✅ Validación")
print("  ✅ Control de acceso")
print("  ✅ Cambios internos sin afectar código externo")

print("\nEjemplo completo:")
print("  class CuentaBancaria:")
print("      def __init__(self, saldo):")
print("          self.__saldo = saldo")
print("")
print("      def obtener_saldo(self):")
print("          return self.__saldo")

print("\n" + "=" * 50)
