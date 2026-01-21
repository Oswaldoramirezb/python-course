"""
DESCRIPTORS: CONCEPTO
=====================
Protocolo de descriptors
"""

print("=" * 50)
print("CONCEPTO DE DESCRIPTORS")
print("=" * 50)

print("\nDescriptor:")
print("  - Objeto que define cómo se accede a atributos")
print("  - Controla get, set, delete")
print("  - Base de properties, métodos estáticos, etc.")

print("\nProtocolo:")
print("  __get__(self, instance, owner) - Obtener valor")
print("  __set__(self, instance, value) - Establecer valor")
print("  __delete__(self, instance) - Eliminar")

print("\nTipos:")
print("  Data descriptor - Tiene __set__ o __delete__")
print("  Non-data descriptor - Solo tiene __get__")

print("\nEjemplo básico:")
print("  class MiDescriptor:")
print("      def __get__(self, instance, owner):")
print("          return valor")
print("")
print("  class MiClase:")
print("      atributo = MiDescriptor()")

print("\nUsos:")
print("  ✅ Properties")
print("  ✅ Validación de datos")
print("  ✅ Lazy evaluation")
print("  ✅ Caché de valores")

print("\nVentajas:")
print("  ✅ Control fino sobre atributos")
print("  ✅ Reutilizable")
print("  ✅ Encapsulación")

print("\n" + "=" * 50)
