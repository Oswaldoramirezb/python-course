"""
SERIALIZACIÓN: OBJETOS PERSONALIZADOS
======================================
Serializar objetos personalizados con JSON
"""

print("=" * 50)
print("SERIALIZAR OBJETOS PERSONALIZADOS")
print("=" * 50)

import json

# Clase personalizada
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def to_dict(self):
        """Convertir a diccionario"""
        return {"nombre": self.nombre, "edad": self.edad}
    
    @classmethod
    def from_dict(cls, datos):
        """Crear desde diccionario"""
        return cls(datos["nombre"], datos["edad"])
    
    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"

persona = Persona("Juan", 30)
print(f"\nObjeto: {persona}")

# Serializar
persona_dict = persona.to_dict()
json_str = json.dumps(persona_dict)
print(f"\nSerializar:")
print(f"  persona.to_dict() = {persona_dict}")
print(f"  json.dumps(persona_dict) = {json_str}")

# Deserializar
datos_recuperados = json.loads(json_str)
persona_recuperada = Persona.from_dict(datos_recuperados)
print(f"\nDeserializar:")
print(f"  persona_recuperada = {persona_recuperada}")

# Con JSONEncoder personalizado
class PersonaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Persona):
            return obj.to_dict()
        return super().default(obj)

persona2 = Persona("María", 25)
json_str2 = json.dumps(persona2, cls=PersonaEncoder)
print(f"\nCon encoder personalizado:")
print(f"  json.dumps(persona2, cls=PersonaEncoder) = {json_str2}")

print("\n" + "=" * 50)
