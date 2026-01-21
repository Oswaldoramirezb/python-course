"""
DATETIME: CONCEPTO
==================
Trabajar con fechas y tiempo en Python
"""

print("=" * 50)
print("CONCEPTO DE DATETIME")
print("=" * 50)

from datetime import datetime, date, time

print("\nMódulo datetime:")
print("  - Trabajar con fechas y horas")
print("  - Calcular diferencias")
print("  - Formatear fechas")

print("\nClases principales:")
print("  datetime - Fecha y hora")
print("  date - Solo fecha")
print("  time - Solo hora")
print("  timedelta - Diferencia de tiempo")

print("\nEjemplo básico:")
print("  from datetime import datetime")
print("  ahora = datetime.now()")
print("  print(ahora)")

ahora = datetime.now()
print(f"\nFecha y hora actual:")
print(f"  datetime.now() = {ahora}")

print("\nUsos comunes:")
print("  ✅ Registrar eventos")
print("  ✅ Calcular edades")
print("  ✅ Programar tareas")
print("  ✅ Analizar datos temporales")

print("\n" + "=" * 50)
