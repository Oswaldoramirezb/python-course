"""
FUNCIÓN: VARIABLES GLOBALES
===========================
Modificar variables globales desde una función
"""

print("=" * 50)
print("VARIABLES GLOBALES")
print("=" * 50)

# Variable global
contador = 0

def incrementar():
    """Incrementa el contador global"""
    global contador
    contador += 1

print(f"\nContador inicial: {contador}")

print("\nIncrementar:")
incrementar()
print(f"  Después de incrementar(): {contador}")

incrementar()
print(f"  Después de incrementar(): {contador}")

# Sin global (error)
def intentar_modificar():
    """Intenta modificar sin global"""
    # contador += 1  # Esto daría error sin 'global'
    pass

print("\n⚠️  IMPORTANTE: Usar 'global' para modificar variables globales")

print("\n" + "=" * 50)
