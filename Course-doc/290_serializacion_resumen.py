"""
RESUMEN: SERIALIZACIÓN
======================
Todas las operaciones de serialización
"""

print("=" * 50)
print("RESUMEN - SERIALIZACIÓN")
print("=" * 50)

print("\nConcepto:")
print("  - Convertir objeto a formato almacenable")
print("  - Guardar o transmitir")
print("  - Deserializar para recuperar")

print("\nJSON:")
print("  import json")
print("  json.dumps(obj) - Serializar a string")
print("  json.loads(str) - Deserializar desde string")
print("  json.dump(obj, file) - Guardar en archivo")
print("  json.load(file) - Leer de archivo")

print("\nPickle:")
print("  import pickle")
print("  pickle.dumps(obj) - Serializar a bytes")
print("  pickle.loads(bytes) - Deserializar desde bytes")
print("  pickle.dump(obj, file) - Guardar en archivo")
print("  pickle.load(file) - Leer de archivo")

print("\nObjetos personalizados:")
print("  - JSON: Convertir a dict (to_dict)")
print("  - Pickle: Funciona directamente")
print("  - JSONEncoder personalizado")

print("\nComparación:")
print("  JSON - Texto, legible, limitado, seguro")
print("  Pickle - Binario, completo, Python, riesgo")

print("\nUsos:")
print("  ✅ Guardar configuración")
print("  ✅ Persistencia de datos")
print("  ✅ APIs y servicios web")
print("  ✅ Comunicación entre procesos")

print("\n" + "=" * 50)
