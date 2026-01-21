"""
FUNCIÓN: PARÁMETROS POR DEFECTO
================================
Parámetros con valores predeterminados
"""

print("=" * 50)
print("PARÁMETROS POR DEFECTO")
print("=" * 50)

# Función con parámetro por defecto
def saludar(nombre, titulo="Sr./Sra."):
    """Saluda con un título opcional"""
    return f"¡Hola, {titulo} {nombre}!"

print("\nParámetro por defecto:")
print(f"  saludar('García') = {saludar('García')}")
print(f"  saludar('López', 'Dr.') = {saludar('López', 'Dr.')}")

# Múltiples parámetros por defecto
def crear_usuario(nombre, email, activo=True, rol="usuario"):
    return f"Usuario: {nombre}, Email: {email}, Activo: {activo}, Rol: {rol}"

print(f"\nMúltiples parámetros por defecto:")
print(f"  crear_usuario('Juan', 'juan@email.com')")
print(f"    = {crear_usuario('Juan', 'juan@email.com')}")
print(f"  crear_usuario('Admin', 'admin@email.com', True, 'admin')")
print(f"    = {crear_usuario('Admin', 'admin@email.com', True, 'admin')}")

print("\n" + "=" * 50)
