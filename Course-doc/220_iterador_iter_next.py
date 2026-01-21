"""
ITERADOR: ITER Y NEXT
=====================
Usar iter() y next() con iteradores
"""

print("=" * 50)
print("ITER() Y NEXT()")
print("=" * 50)

# Crear iterador desde iterable
lista = [1, 2, 3, 4, 5]
print(f"\nLista: {lista}")

iterador = iter(lista)
print(f"\nCrear iterador:")
print(f"  iterador = iter(lista)")

print("\nObtener valores con next():")
print(f"  next(iterador) = {next(iterador)}")
print(f"  next(iterador) = {next(iterador)}")
print(f"  next(iterador) = {next(iterador)}")

# StopIteration
print("\nCuando se agota:")
try:
    for _ in range(3):
        next(iterador)
except StopIteration:
    print("  ✅ StopIteration: El iterador se agotó")

# Con cadena
texto = "Python"
iterador_texto = iter(texto)
print(f"\nCon cadena '{texto}':")
print(f"  next(iterador_texto) = {next(iterador_texto)}")
print(f"  next(iterador_texto) = {next(iterador_texto)}")

# next() con valor por defecto
iterador2 = iter([1, 2])
print(f"\nnext() con valor por defecto:")
print(f"  next(iterador2, 'Fin') = {next(iterador2, 'Fin')}")
print(f"  next(iterador2, 'Fin') = {next(iterador2, 'Fin')}")
print(f"  next(iterador2, 'Fin') = {next(iterador2, 'Fin')} (valor por defecto)")

print("\n" + "=" * 50)
