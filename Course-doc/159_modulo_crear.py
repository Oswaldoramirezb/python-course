"""
MÓDULO: CREAR
=============
Crear tus propios módulos
"""

print("=" * 50)
print("CREAR MÓDULOS")
print("=" * 50)

# Crear un módulo simple
print("\nPara crear un módulo:")
print("  1. Crear archivo mi_modulo.py")
print("  2. Escribir funciones/clases en el archivo")
print("  3. Importar: import mi_modulo")

# Ejemplo de estructura
print("\nEjemplo - mi_modulo.py:")
print("  def saludar(nombre):")
print("      return f'Hola, {nombre}!'")
print("")
print("  def sumar(a, b):")
print("      return a + b")
print("")
print("  PI = 3.14159")

# Usar el módulo
print("\nUsar el módulo:")
print("  import mi_modulo")
print("  mi_modulo.saludar('Juan')")
print("  mi_modulo.sumar(5, 3)")

# O con from import
print("\nO con from import:")
print("  from mi_modulo import saludar, sumar")
print("  saludar('Juan')")
print("  sumar(5, 3)")

print("\n" + "=" * 50)
