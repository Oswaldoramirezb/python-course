"""
CLASE: MÉTODOS DE CLASE
=======================
Métodos que trabajan con la clase, no con instancias
"""

print("=" * 50)
print("MÉTODOS DE CLASE")
print("=" * 50)

class Persona:
    contador = 0
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.contador += 1
    
    @classmethod
    def obtener_contador(cls):
        """Método de clase: recibe cls (la clase)"""
        return cls.contador
    
    @classmethod
    def crear_desde_string(cls, cadena):
        """Método de clase alternativo para crear instancias"""
        # Ejemplo: "Juan:30"
        nombre, edad = cadena.split(":")
        return cls(nombre, int(edad))

print("\nMétodo de clase:")
print("  @classmethod")
print("  def metodo(cls):")
print("      return cls.contador")

print("\nLlamar método de clase:")
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)
print(f"  Persona.obtener_contador() = {Persona.obtener_contador()}")

print("\nMétodo de clase para crear objetos:")
persona3 = Persona.crear_desde_string("Pedro:28")
print(f"  Persona.crear_desde_string('Pedro:28')")
print(f"  persona3.nombre = {persona3.nombre}, edad = {persona3.edad}")

print("\n" + "=" * 50)
