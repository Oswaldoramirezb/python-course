"""
DICCIONARIO: ELIMINAR
=====================
Eliminar elementos de un diccionario
"""

print("=" * 50)
print("ELIMINAR ELEMENTOS DE DICCIONARIO")
print("=" * 50)

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid", "email": "juan@email.com"}
print(f"\nDiccionario original: {persona}")

# del - eliminar por clave
del persona["email"]
print(f"Después de del persona['email']: {persona}")

# pop() - eliminar y retornar valor
edad = persona.pop("edad")
print(f"Después de pop('edad'): {persona}, edad eliminada: {edad}")

# popitem() - eliminar último elemento
clave, valor = persona.popitem()
print(f"Después de popitem(): {persona}, eliminado: {clave}={valor}")

# clear() - vaciar diccionario
persona.clear()
print(f"Después de clear(): {persona}")

print("\n" + "=" * 50)
