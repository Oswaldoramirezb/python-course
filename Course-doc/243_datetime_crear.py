"""
DATETIME: CREAR
===============
Crear objetos de fecha y hora
"""

print("=" * 50)
print("CREAR FECHAS Y HORAS")
print("=" * 50)

from datetime import datetime, date, time

# datetime.now() - fecha y hora actual
ahora = datetime.now()
print("\ndatetime.now():")
print(f"  {ahora}")

# datetime específico
fecha_especifica = datetime(2024, 1, 15, 14, 30, 0)
print("\ndatetime específico:")
print(f"  datetime(2024, 1, 15, 14, 30, 0) = {fecha_especifica}")

# date - solo fecha
fecha = date(2024, 1, 15)
print("\ndate (solo fecha):")
print(f"  date(2024, 1, 15) = {fecha}")

# time - solo hora
hora = time(14, 30, 0)
print("\ntime (solo hora):")
print(f"  time(14, 30, 0) = {hora}")

# Combinar date y time
fecha_hora = datetime.combine(fecha, hora)
print("\nCombinar date y time:")
print(f"  datetime.combine(fecha, hora) = {fecha_hora}")

print("\n" + "=" * 50)
