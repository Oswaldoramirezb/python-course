"""
LISTA: COPIAR
=============
Copiar listas (importante: copia vs referencia)
"""

print("=" * 50)
print("COPIAR LISTAS")
print("=" * 50)

lista_original = [1, 2, 3]
print(f"\nLista original: {lista_original}")

# Copia superficial
copia1 = lista_original.copy()
copia2 = lista_original[:]
copia3 = list(lista_original)

print(f"  copia1 = lista_original.copy() → {copia1}")
print(f"  copia2 = lista_original[:] → {copia2}")
print(f"  copia3 = list(lista_original) → {copia3}")

# Modificar copia no afecta original
copia1[0] = 10
print(f"\nDespués de copia1[0] = 10:")
print(f"  original: {lista_original}")
print(f"  copia1: {copia1}")

# ⚠️ Asignación directa NO es copia
referencia = lista_original
referencia[0] = 99
print(f"\n⚠️  referencia = lista_original (NO es copia):")
print(f"  original: {lista_original} (se modificó!)")
print(f"  referencia: {referencia}")

print("\n" + "=" * 50)
