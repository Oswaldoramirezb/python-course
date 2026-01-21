"""
HASHABLES: CONCEPTO
===================
¿Qué objetos son hashables?
"""

print("=" * 50)
print("CONCEPTO DE HASHABLES")
print("=" * 50)

print("\nHashable:")
print("  - Objeto que tiene hash")
print("  - Puede ser clave en dict o elemento en set")
print("  - Debe ser inmutable")

print("\nTipos hashables:")
print("  ✅ int, float, str, bool")
print("  ✅ tuple (si todos sus elementos son hashables)")
print("  ✅ frozenset")
print("  ✅ None")

print("\nTipos NO hashables:")
print("  ❌ list")
print("  ❌ dict")
print("  ❌ set")
print("  ❌ Objetos mutables personalizados")

# Verificar si es hashable
print("\nVerificar si es hashable:")
tipos = [42, "texto", (1, 2), [1, 2], {1, 2}]

for tipo in tipos:
    try:
        hash(tipo)
        print(f"  {type(tipo).__name__}: ✅ Hashable")
    except TypeError:
        print(f"  {type(tipo).__name__}: ❌ No hashable")

print("\nUso en diccionarios:")
print("  dict[clave_hashable] = valor")
print("  dict[123] = 'OK' ✅")
print("  dict[[1,2]] = 'Error' ❌")

print("\n" + "=" * 50)
