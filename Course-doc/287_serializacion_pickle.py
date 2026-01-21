"""
SERIALIZACIÓN: PICKLE
=====================
Serializar y deserializar con Pickle
"""

print("=" * 50)
print("PICKLE - SERIALIZACIÓN")
print("=" * 50)

import pickle

# Serializar objeto Python
datos = {
    "nombre": "Juan",
    "edad": 30,
    "lista": [1, 2, 3],
    "tupla": (4, 5, 6)
}

pickle_data = pickle.dumps(datos)
print("\nSerializar (dumps):")
print(f"  datos = {datos}")
print(f"  pickle.dumps(datos) = {pickle_data[:50]}... (binario)")

# Deserializar
datos_recuperados = pickle.loads(pickle_data)
print("\nDeserializar (loads):")
print(f"  pickle.loads(pickle_data) = {datos_recuperados}")

# Con objetos personalizados
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"

persona = Persona("María", 25)
pickle_persona = pickle.dumps(persona)
persona_recuperada = pickle.loads(pickle_persona)

print("\nCon objetos personalizados:")
print(f"  persona = {persona}")
print(f"  persona_recuperada = {persona_recuperada}")

# Guardar en archivo
with open("datos.pkl", "wb") as f:
    pickle.dump(datos, f)

print("\nGuardar en archivo (binario):")
print("  with open('datos.pkl', 'wb') as f:")
print("      pickle.dump(datos, f)")

# Leer de archivo
with open("datos.pkl", "rb") as f:
    datos_leidos = pickle.load(f)

print(f"\nLeer de archivo:")
print(f"  datos_leidos = {datos_leidos}")

print("\n⚠️  SEGURIDAD:")
print("  - Pickle puede ejecutar código")
print("  - Solo usar con datos confiables")
print("  - No usar con datos de fuentes desconocidas")

print("\n" + "=" * 50)
