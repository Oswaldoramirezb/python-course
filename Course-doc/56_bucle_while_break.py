"""
BUCLE WHILE: BREAK
==================
Salir del bucle while antes de tiempo
"""

print("=" * 50)
print("BUCLE WHILE CON BREAK")
print("=" * 50)

# While con break
print("\nEjemplo 1 - Salir cuando llegue a 5:")
contador = 0
while True:  # Bucle infinito
    print(f"  Contador: {contador}")
    contador += 1
    if contador >= 5:
        print("  ⚠️  Llegamos a 5, saliendo...")
        break

# Menú interactivo (simulado)
print("\nEjemplo 2 - Menú interactivo:")
opcion = 1
while opcion != 0:
    print(f"  Opción actual: {opcion}")
    if opcion == 1:
        print("    Ejecutando opción 1...")
    elif opcion == 2:
        print("    Ejecutando opción 2...")
    opcion += 1
    if opcion > 2:
        opcion = 0
        print("  Saliendo del menú...")

print("\n" + "=" * 50)
