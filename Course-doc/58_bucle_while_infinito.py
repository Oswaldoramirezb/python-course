"""
BUCLE WHILE: INFINITO
=====================
Bucle que se ejecuta indefinidamente (usar con cuidado)
"""

print("=" * 50)
print("BUCLE WHILE INFINITO")
print("=" * 50)

# While True - bucle infinito controlado
print("\nEjemplo 1 - Bucle infinito con break:")
contador = 0
while True:
    print(f"  Iteración: {contador}")
    contador += 1
    if contador >= 3:  # Control para no ejecutar infinitamente
        print("  ⚠️  Saliendo del bucle infinito...")
        break

# Menú que se repite hasta salir
print("\nEjemplo 2 - Menú repetitivo (simulado):")
opcion = "continuar"
iteracion = 0
while opcion != "salir":
    iteracion += 1
    print(f"  Iteración {iteracion} del menú")
    if iteracion >= 3:  # Control
        opcion = "salir"
        print("  Saliendo...")

print("\n⚠️  IMPORTANTE: Siempre tener una forma de salir (break o condición)")

print("\n" + "=" * 50)
