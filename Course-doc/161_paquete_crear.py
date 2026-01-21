"""
PAQUETE: CREAR
==============
Crear paquetes (carpetas con módulos)
"""

print("=" * 50)
print("CREAR PAQUETES")
print("=" * 50)

# Estructura de paquete
print("\nEstructura de un paquete:")
print("  mi_paquete/")
print("      __init__.py  (hace que sea un paquete)")
print("      modulo1.py")
print("      modulo2.py")
print("      subpaquete/")
print("          __init__.py")
print("          modulo3.py")

# __init__.py
print("\n__init__.py:")
print("  - Hace que una carpeta sea un paquete")
print("  - Puede estar vacío o contener código de inicialización")

# Importar de paquete
print("\nImportar de paquete:")
print("  from mi_paquete import modulo1")
print("  from mi_paquete.modulo1 import funcion")
print("  from mi_paquete.subpaquete import modulo3")

# Ejemplo
print("\nEjemplo:")
print("  import mi_paquete.modulo1")
print("  mi_paquete.modulo1.funcion()")

print("\n" + "=" * 50)
