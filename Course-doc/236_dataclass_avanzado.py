"""
DATACLASS: AVANZADO
===================
Opciones avanzadas de dataclasses
"""

print("=" * 50)
print("DATACLASS AVANZADO")
print("=" * 50)

from dataclasses import dataclass, field

# Dataclass con opciones
@dataclass(frozen=True)  # Inmutable
class Punto:
    x: int
    y: int

punto = Punto(3, 4)
print("\nDataclass frozen (inmutable):")
print(f"  punto = {punto}")
print("  punto.x = 5  # ❌ Error: frozen=True")

# Dataclass con field()
@dataclass
class Persona:
    nombre: str
    edad: int
    amigos: list[str] = field(default_factory=list)
    _id: int = field(init=False, repr=False)  # No en __init__, no en __repr__
    
    def __post_init__(self):
        """Se ejecuta después de __init__"""
        self._id = hash(self.nombre)

persona = Persona("Juan", 30)
persona.amigos.append("Pedro")
print("\nDataclass con field():")
print(f"  persona = {persona}")
print(f"  persona.amigos = {persona.amigos}")

# Dataclass con orden
@dataclass(order=True)
class Producto:
    precio: float
    nombre: str

producto1 = Producto(10.5, "A")
producto2 = Producto(5.3, "B")
print("\nDataclass con order=True:")
print(f"  producto1 < producto2 = {producto1 < producto2}")

print("\n" + "=" * 50)
