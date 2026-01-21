"""
TIMEDELTA: DIFERENCIAS DE TIEMPO
=================================
Calcular diferencias y sumar/restar tiempo
"""

print("=" * 50)
print("TIMEDELTA")
print("=" * 50)

from datetime import datetime, timedelta

# Crear timedelta
ahora = datetime.now()
print(f"\nFecha actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")

# Sumar tiempo
futuro = ahora + timedelta(days=7)
print(f"\nSumar 7 días:")
print(f"  ahora + timedelta(days=7) = {futuro.strftime('%Y-%m-%d')}")

# Restar tiempo
pasado = ahora - timedelta(days=30)
print(f"\nRestar 30 días:")
print(f"  ahora - timedelta(days=30) = {pasado.strftime('%Y-%m-%d')}")

# Múltiples unidades
futuro2 = ahora + timedelta(days=1, hours=2, minutes=30)
print(f"\nSumar múltiples unidades:")
print(f"  ahora + timedelta(days=1, hours=2, minutes=30)")
print(f"    = {futuro2.strftime('%Y-%m-%d %H:%M:%S')}")

# Diferencia entre fechas
fecha1 = datetime(2024, 1, 1)
fecha2 = datetime(2024, 1, 15)
diferencia = fecha2 - fecha1
print(f"\nDiferencia:")
print(f"  fecha2 - fecha1 = {diferencia}")
print(f"  diferencia.days = {diferencia.days} días")
print(f"  diferencia.total_seconds() = {diferencia.total_seconds()} segundos")

print("\n" + "=" * 50)
