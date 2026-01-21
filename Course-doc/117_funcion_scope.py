"""
FUNCIÓN: SCOPE (ALCANCE)
========================
Alcance de variables en funciones
"""

print("=" * 50)
print("SCOPE - ALCANCE DE VARIABLES")
print("=" * 50)

# Variable global
variable_global = "Soy global"

def funcion_scope():
    """Demuestra el alcance de variables"""
    # Variable local
    variable_local = "Soy local"
    print(f"  Dentro de la función:")
    print(f"    variable_global = {variable_global}")
    print(f"    variable_local = {variable_local}")

print("\nVariable global:")
print(f"  variable_global = '{variable_global}'")

print("\nDentro de la función:")
funcion_scope()

print(f"\nFuera de la función:")
print(f"  variable_global = '{variable_global}'")
print(f"  variable_local → Error (no existe fuera)")

print("\n" + "=" * 50)
