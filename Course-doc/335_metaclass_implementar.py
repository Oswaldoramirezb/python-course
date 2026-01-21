"""
METACLASS: IMPLEMENTAR
======================
Crear metaclasses personalizadas
"""

print("=" * 50)
print("IMPLEMENTAR METACLASS")
print("=" * 50)

# Metaclass que registra clases
clases_registradas = []

class RegistrarMetaclass(type):
    """Metaclass que registra clases automáticamente"""
    def __new__(cls, name, bases, attrs):
        nueva_clase = super().__new__(cls, name, bases, attrs)
        clases_registradas.append(nueva_clase)
        print(f"  ✅ Clase '{name}' registrada")
        return nueva_clase

# Usar metaclass
class Animal(metaclass=RegistrarMetaclass):
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    pass

class Gato(Animal):
    pass

print("\nMetaclass que registra:")
print("  class RegistrarMetaclass(type):")
print("      def __new__(cls, name, bases, attrs):")
print("          nueva_clase = super().__new__(cls, name, bases, attrs)")
print("          clases_registradas.append(nueva_clase)")
print("          return nueva_clase")

print(f"\nClases registradas: {[c.__name__ for c in clases_registradas]}")

# Metaclass que valida atributos
class ValidarAtributosMetaclass(type):
    """Metaclass que valida que ciertos atributos existan"""
    def __new__(cls, name, bases, attrs):
        # Validar que tenga método requerido
        if 'metodo_requerido' not in attrs:
            raise TypeError(f"La clase {name} debe tener 'metodo_requerido'")
        return super().__new__(cls, name, bases, attrs)

print("\nMetaclass que valida:")
print("  class ValidarAtributosMetaclass(type):")
print("      def __new__(cls, name, bases, attrs):")
print("          if 'metodo_requerido' not in attrs:")
print("              raise TypeError(...)")

class ClaseValida(metaclass=ValidarAtributosMetaclass):
    def metodo_requerido(self):
        return "OK"

print("  ✅ Clase válida creada")

print("\nUsos comunes:")
print("  ✅ ORMs (SQLAlchemy)")
print("  ✅ Frameworks (Django)")
print("  ✅ Validación de esquemas")
print("  ✅ Registro automático")

print("\n⚠️  ADVERTENCIA:")
print("  - Muy avanzado")
print("  - Usar solo cuando sea necesario")
print("  - Decoradores suelen ser suficientes")

print("\n" + "=" * 50)
