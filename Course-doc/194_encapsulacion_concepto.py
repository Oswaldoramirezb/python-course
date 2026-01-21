"""
ENCAPSULACIÓN: CONCEPTO
=======================
Ocultar detalles internos y proteger datos
"""

print("=" * 50)
print("CONCEPTO DE ENCAPSULACIÓN")
print("=" * 50)

print("\nEncapsulación significa:")
print("  - Ocultar detalles de implementación")
print("  - Proteger datos internos")
print("  - Controlar acceso a atributos y métodos")

print("\nNiveles de acceso en Python:")
print("  Público      - Accesible desde cualquier lugar")
print("  Protegido    - Convención: _atributo (un guion bajo)")
print("  Privado      - Convención: __atributo (dos guiones bajos)")

print("\nEjemplo:")
print("  class CuentaBancaria:")
print("      def __init__(self, saldo):")
print("          self.__saldo = saldo  # Privado")
print("")
print("      def obtener_saldo(self):  # Método público")
print("          return self.__saldo")

print("\nVentajas:")
print("  ✅ Protección de datos")
print("  ✅ Control de acceso")
print("  ✅ Validación de datos")
print("  ✅ Cambios internos sin afectar código externo")

print("\n" + "=" * 50)
