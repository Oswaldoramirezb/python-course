"""
MÓDULO: __NAME__ == '__MAIN__'
================================
Ejecutar código solo cuando se ejecuta directamente
"""

print("=" * 50)
print("__NAME__ == '__MAIN__'")
print("=" * 50)

# __name__ y __main__
print("\n__name__ es una variable especial:")
print("  - Si ejecutas el archivo directamente: __name__ = '__main__'")
print("  - Si lo importas: __name__ = 'nombre_del_modulo'")

# Ejemplo práctico
print("\nEjemplo - mi_modulo.py:")
print("  def funcion_util():")
print("      return 'Función útil'")
print("")
print("  if __name__ == '__main__':")
print("      print('Este código solo se ejecuta si se ejecuta directamente')")
print("      print('No se ejecuta si se importa')")

# Simulación
def funcion_util():
    return "Función útil"

if __name__ == "__main__":
    print("\n  ✅ Este código se ejecuta porque __name__ == '__main__'")
    print(f"  {funcion_util()}")

print("\nVentajas:")
print("  ✅ Código de prueba solo cuando se ejecuta directamente")
print("  ✅ Módulo reutilizable sin ejecutar código de prueba")

print("\n" + "=" * 50)
