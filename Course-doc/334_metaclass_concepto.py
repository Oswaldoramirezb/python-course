"""
METACLASS: CONCEPTO
===================
Clases que crean clases
"""

print("=" * 50)
print("CONCEPTO DE METACLASS")
print("=" * 50)

print("\nMetaclass:")
print("  - Clase que crea clases")
print("  - 'Clase de clases'")
print("  - Controla creación de clases")

print("\nJerarquía:")
print("  type - Metaclass por defecto")
print("  class MiClase - Creada por type")
print("  objeto = MiClase() - Instancia de MiClase")

print("\nEjemplo básico:")
print("  class MiMetaclass(type):")
print("      def __new__(cls, name, bases, attrs):")
print("          # Modificar creación de clase")
print("          return super().__new__(cls, name, bases, attrs)")

print("\nUsos:")
print("  ✅ Registrar clases automáticamente")
print("  ✅ Validar atributos")
print("  ✅ Agregar métodos automáticamente")
print("  ✅ ORMs (SQLAlchemy)")
print("  ✅ Frameworks (Django)")

print("\nEjemplo - Registrar clases:")
print("  clases_registradas = []")
print("")
print("  class RegistrarMetaclass(type):")
print("      def __new__(cls, name, bases, attrs):")
print("          nueva_clase = super().__new__(cls, name, bases, attrs)")
print("          clases_registradas.append(nueva_clase)")
print("          return nueva_clase")

print("\n⚠️  IMPORTANTE:")
print("  - Avanzado y complejo")
print("  - Usar solo cuando sea necesario")
print("  - Decoradores suelen ser suficientes")

print("\n" + "=" * 50)
