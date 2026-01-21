"""
SERIALIZACIÓN: CONCEPTO
=======================
Convertir objetos a formato almacenable
"""

print("=" * 50)
print("CONCEPTO DE SERIALIZACIÓN")
print("=" * 50)

import json
import pickle

print("\nSerialización:")
print("  - Convertir objeto a formato almacenable")
print("  - Guardar en archivo o enviar por red")
print("  - Deserializar para recuperar objeto")

print("\nFormatos comunes:")
print("  JSON - Texto, legible, limitado")
print("  Pickle - Binario, Python específico, completo")
print("  XML - Texto, estructurado")
print("  YAML - Texto, legible")

print("\nEjemplo JSON:")
datos = {"nombre": "Juan", "edad": 30}
json_str = json.dumps(datos)
print(f"  datos = {datos}")
print(f"  json.dumps(datos) = {json_str}")

print("\nEjemplo Pickle:")
datos_pickle = pickle.dumps(datos)
print(f"  pickle.dumps(datos) = {datos_pickle[:50]}... (binario)")

print("\nUsos:")
print("  ✅ Guardar configuración")
print("  ✅ Persistencia de datos")
print("  ✅ Comunicación entre procesos")
print("  ✅ APIs y servicios web")

print("\n" + "=" * 50)
