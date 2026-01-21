"""
SERIALIZACIÓN: JSON
===================
Serializar y deserializar con JSON
"""

print("=" * 50)
print("JSON - SERIALIZACIÓN")
print("=" * 50)

import json

# Serializar (objeto → JSON string)
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "activo": True,
    "hijos": ["Ana", "Pedro"]
}

json_str = json.dumps(datos, indent=2)
print("\nSerializar (dumps):")
print(f"  datos = {datos}")
print(f"  json.dumps(datos, indent=2):")
print(json_str)

# Deserializar (JSON string → objeto)
json_texto = '{"nombre": "María", "edad": 25}'
datos_recuperados = json.loads(json_texto)
print("\nDeserializar (loads):")
print(f"  json_texto = '{json_texto}'")
print(f"  json.loads(json_texto) = {datos_recuperados}")

# Guardar en archivo
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2)

print("\nGuardar en archivo:")
print("  with open('datos.json', 'w') as f:")
print("      json.dump(datos, f)")

# Leer de archivo
with open("datos.json", "r", encoding="utf-8") as f:
    datos_leidos = json.load(f)

print("\nLeer de archivo:")
print(f"  datos_leidos = {datos_leidos}")

print("\nLimitaciones JSON:")
print("  ❌ Solo tipos básicos (dict, list, str, int, float, bool, None)")
print("  ❌ No objetos personalizados directamente")
print("  ✅ Solución: Convertir a dict primero")

print("\n" + "=" * 50)
