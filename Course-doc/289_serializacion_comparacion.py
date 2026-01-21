"""
SERIALIZACIÓN: COMPARACIÓN
==========================
Comparar JSON vs Pickle
"""

print("=" * 50)
print("COMPARACIÓN JSON VS PICKLE")
print("=" * 50)

import json
import pickle

datos = {
    "nombre": "Juan",
    "edad": 30,
    "lista": [1, 2, 3]
}

print(f"\nDatos: {datos}")

# JSON
json_str = json.dumps(datos)
print(f"\nJSON:")
print(f"  Tipo: Texto (string)")
print(f"  Tamaño: {len(json_str)} bytes")
print(f"  Legible: ✅ Sí")
print(f"  Ejemplo: {json_str}")

# Pickle
pickle_data = pickle.dumps(datos)
print(f"\nPickle:")
print(f"  Tipo: Binario (bytes)")
print(f"  Tamaño: {len(pickle_data)} bytes")
print(f"  Legible: ❌ No")
print(f"  Ejemplo: {pickle_data[:50]}...")

print("\nComparación:")
print("  JSON:")
print("    ✅ Legible por humanos")
print("    ✅ Compatible entre lenguajes")
print("    ✅ Seguro")
print("    ❌ Solo tipos básicos")
print("")
print("  Pickle:")
print("    ✅ Cualquier objeto Python")
print("    ✅ Más compacto")
print("    ❌ Solo Python")
print("    ❌ Riesgo de seguridad")

print("\nCuándo usar:")
print("  JSON - APIs, configuraciones, datos simples")
print("  Pickle - Objetos complejos, Python interno")

print("\n" + "=" * 50)
