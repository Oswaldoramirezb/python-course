"""
DICCIONARIO: ANIDADOS
=====================
Diccionarios dentro de diccionarios
"""

print("=" * 50)
print("DICCIONARIOS ANIDADOS")
print("=" * 50)

# Diccionario anidado
estudiantes = {
    "estudiante1": {"nombre": "Ana", "nota": 85},
    "estudiante2": {"nombre": "Luis", "nota": 92}
}
print(f"\nDiccionario anidado: {estudiantes}")

# Acceder a elementos anidados
print(f"  estudiantes['estudiante1']['nombre'] = {estudiantes['estudiante1']['nombre']}")
print(f"  estudiantes['estudiante1']['nota'] = {estudiantes['estudiante1']['nota']}")

# Modificar elemento anidado
estudiantes["estudiante1"]["nota"] = 90
print(f"\nDespués de modificar nota: {estudiantes['estudiante1']}")

# Iterar sobre anidados
print(f"\nIterar sobre anidados:")
for estudiante_id, datos in estudiantes.items():
    print(f"  {estudiante_id}: {datos['nombre']} - Nota: {datos['nota']}")

print("\n" + "=" * 50)
