"""
GENERADOR: NEXT
===============
Obtener el siguiente valor con next()
"""

print("=" * 50)
print("GENERADOR CON NEXT()")
print("=" * 50)

# Generador
def contar():
    for i in range(1, 4):
        yield i

gen = contar()
print("\nGenerador:")
print("  gen = contar()")

print("\nObtener valores con next():")
print(f"  next(gen) = {next(gen)}")
print(f"  next(gen) = {next(gen)}")
print(f"  next(gen) = {next(gen)}")

# StopIteration
print("\nCuando se agota:")
try:
    next(gen)
except StopIteration:
    print("  ✅ StopIteration: El generador se agotó")

# next() con valor por defecto
def contar_limitado():
    for i in range(2):
        yield i

gen2 = contar_limitado()
print("\nnext() con valor por defecto:")
print(f"  next(gen2, 'Fin') = {next(gen2, 'Fin')}")
print(f"  next(gen2, 'Fin') = {next(gen2, 'Fin')}")
print(f"  next(gen2, 'Fin') = {next(gen2, 'Fin')} (valor por defecto)")

print("\nUso común:")
print("  - Obtener valores uno por uno")
print("  - Control manual del generador")
print("  - Procesar secuencias grandes en partes")

print("\n" + "=" * 50)
