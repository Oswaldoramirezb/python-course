"""
MÓDULO: FROM IMPORT
====================
Importar elementos específicos de un módulo
"""

print("=" * 50)
print("FROM IMPORT")
print("=" * 50)

# from import básico
from math import pi, sqrt, cos
print("\nfrom math import pi, sqrt, cos:")
print(f"  pi = {pi}")
print(f"  sqrt(16) = {sqrt(16)}")
print(f"  cos(0) = {cos(0)}")

# from import con alias
from math import pi as PI, sqrt as raiz_cuadrada
print("\nfrom import con alias:")
print(f"  PI = {PI}")
print(f"  raiz_cuadrada(9) = {raiz_cuadrada(9)}")

# from import todo (no recomendado)
print("\nfrom import * (no recomendado):")
print("  from math import *")
print("  ⚠️  Puede causar conflictos de nombres")

# Comparación
print("\nComparación:")
print("  import math → math.pi")
print("  from math import pi → pi")

print("\n" + "=" * 50)
