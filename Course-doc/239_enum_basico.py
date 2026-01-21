"""
ENUM: BÁSICO
============
Crear y usar enumeraciones básicas
"""

print("=" * 50)
print("ENUM BÁSICO")
print("=" * 50)

from enum import Enum

# Enum básico
class Estado(Enum):
    ACTIVO = 1
    INACTIVO = 2
    PENDIENTE = 3

print("\nEnum básico:")
print("  class Estado(Enum):")
print("      ACTIVO = 1")
print("      INACTIVO = 2")
print("      PENDIENTE = 3")

print("\nUsar enum:")
print(f"  Estado.ACTIVO = {Estado.ACTIVO}")
print(f"  Estado.ACTIVO.name = {Estado.ACTIVO.name}")
print(f"  Estado.ACTIVO.value = {Estado.ACTIVO.value}")

# Comparar
print("\nComparar:")
print(f"  Estado.ACTIVO == Estado.ACTIVO = {Estado.ACTIVO == Estado.ACTIVO}")
print(f"  Estado.ACTIVO == Estado.INACTIVO = {Estado.ACTIVO == Estado.INACTIVO}")

# Iterar
print("\nIterar sobre enum:")
for estado in Estado:
    print(f"  {estado.name} = {estado.value}")

print("\n" + "=" * 50)
