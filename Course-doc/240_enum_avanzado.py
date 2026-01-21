"""
ENUM: AVANZADO
==============
Enumeraciones con funcionalidades avanzadas
"""

print("=" * 50)
print("ENUM AVANZADO")
print("=" * 50)

from enum import Enum, auto, IntEnum

# Enum con auto()
class Color(Enum):
    ROJO = auto()
    VERDE = auto()
    AZUL = auto()

print("\nEnum con auto():")
print("  class Color(Enum):")
print("      ROJO = auto()")
print("      VERDE = auto()")
print("      AZUL = auto()")

print("\nValores automáticos:")
for color in Color:
    print(f"  {color.name} = {color.value}")

# IntEnum (puede compararse con enteros)
class Prioridad(IntEnum):
    BAJA = 1
    MEDIA = 2
    ALTA = 3

print("\nIntEnum (comparable con enteros):")
print(f"  Prioridad.ALTA = {Prioridad.ALTA}")
print(f"  Prioridad.ALTA > 2 = {Prioridad.ALTA > 2}")

# Enum con métodos
class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7
    
    def es_fin_de_semana(self):
        return self in [DiaSemana.SABADO, DiaSemana.DOMINGO]

print("\nEnum con métodos:")
print(f"  DiaSemana.LUNES.es_fin_de_semana() = {DiaSemana.LUNES.es_fin_de_semana()}")
print(f"  DiaSemana.SABADO.es_fin_de_semana() = {DiaSemana.SABADO.es_fin_de_semana()}")

print("\n" + "=" * 50)
