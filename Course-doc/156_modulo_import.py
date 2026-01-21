"""
MÓDULO: IMPORT
==============
Importar módulos en Python
"""

print("=" * 50)
print("IMPORTAR MÓDULOS")
print("=" * 50)

# import básico
import math
print("\nimport math:")
print(f"  math.pi = {math.pi}")
print(f"  math.sqrt(16) = {math.sqrt(16)}")

# import múltiples
import os, sys
print("\nimport múltiples:")
print(f"  os.getcwd() = {os.getcwd()[:50]}...")

# import con alias
import datetime as dt
print("\nimport con alias:")
print(f"  datetime.datetime.now() → dt.datetime.now()")
print(f"  Fecha actual: {dt.datetime.now().strftime('%Y-%m-%d')}")

# import específico
from math import pi, sqrt
print("\nfrom math import pi, sqrt:")
print(f"  pi = {pi}")
print(f"  sqrt(25) = {sqrt(25)}")

print("\n" + "=" * 50)
