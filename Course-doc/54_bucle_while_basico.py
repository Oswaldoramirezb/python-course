"""
BUCLE WHILE: BÁSICO
==================
Repetir mientras una condición sea True
"""

print("=" * 50)
print("BUCLE WHILE BÁSICO")
print("=" * 50)

# While básico
print("\nEjemplo 1 - Contar del 0 al 4:")
contador = 0
while contador < 5:
    print(f"  Contador: {contador}")
    contador += 1

# While con condición
print("\nEjemplo 2 - Contar hacia atrás:")
numero = 10
while numero > 0:
    print(f"  Número: {numero}")
    numero -= 2

print("\n" + "=" * 50)
