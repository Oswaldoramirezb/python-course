"""
ARCHIVO: JSON
=============
Trabajar con archivos JSON
"""

print("=" * 50)
print("ARCHIVOS JSON")
print("=" * 50)

import json

# Escribir JSON
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["leer", "programar", "viajar"]
}

print("\nEscribir JSON:")
with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print("  ✅ Datos escritos en datos.json")

# Leer JSON
print("\nLeer JSON:")
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos_leidos = json.load(archivo)
    print(f"  Datos leídos: {datos_leidos}")

# Convertir a/desde string
print("\nConvertir a/desde string:")
json_string = json.dumps(datos, indent=2)
print(f"  json.dumps(datos) = {json_string[:50]}...")

datos_desde_string = json.loads(json_string)
print(f"  json.loads(json_string) = {datos_desde_string['nombre']}")

print("\n" + "=" * 50)
