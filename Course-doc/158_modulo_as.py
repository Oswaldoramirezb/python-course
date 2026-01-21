"""
MÓDULO: AS (ALIAS)
==================
Dar nombres alternativos a módulos
"""

print("=" * 50)
print("ALIAS CON 'AS'")
print("=" * 50)

# import as
import datetime as dt
print("\nimport datetime as dt:")
print(f"  dt.datetime.now() = {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# import con alias largo
import numpy as np
print("\nimport numpy as np:")
print("  np.array([1, 2, 3])")
print("  (convención común para numpy)")

# from import as
from math import pi as PI, sqrt as SQRT
print("\nfrom math import pi as PI, sqrt as SQRT:")
print(f"  PI = {PI}")
print(f"  SQRT(25) = {SQRT(25)}")

# Ventajas de usar alias
print("\nVentajas de usar alias:")
print("  ✅ Nombres más cortos")
print("  ✅ Evitar conflictos de nombres")
print("  ✅ Convenciones comunes (np, pd, plt)")

print("\n" + "=" * 50)
