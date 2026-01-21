"""
DATETIME: OPERACIONES
=====================
Operaciones con fechas y horas
"""

print("=" * 50)
print("OPERACIONES CON FECHAS")
print("=" * 50)

from datetime import datetime, timedelta

# Fechas
fecha1 = datetime(2024, 1, 15)
fecha2 = datetime(2024, 1, 20)

print("\nFechas:")
print(f"  fecha1 = {fecha1.date()}")
print(f"  fecha2 = {fecha2.date()}")

# Diferencia
diferencia = fecha2 - fecha1
print(f"\nDiferencia:")
print(f"  fecha2 - fecha1 = {diferencia}")
print(f"  diferencia.days = {diferencia.days} días")

# Comparar fechas
print(f"\nComparar:")
print(f"  fecha1 < fecha2 = {fecha1 < fecha2}")
print(f"  fecha1 > fecha2 = {fecha1 > fecha2}")

# Acceder a componentes
ahora = datetime.now()
print(f"\nComponentes de fecha:")
print(f"  ahora.year = {ahora.year}")
print(f"  ahora.month = {ahora.month}")
print(f"  ahora.day = {ahora.day}")
print(f"  ahora.hour = {ahora.hour}")
print(f"  ahora.minute = {ahora.minute}")

print("\n" + "=" * 50)
