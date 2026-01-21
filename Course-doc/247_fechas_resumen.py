"""
RESUMEN: FECHAS Y TIEMPO
========================
Todas las operaciones con fechas
"""

print("=" * 50)
print("RESUMEN - FECHAS Y TIEMPO")
print("=" * 50)

print("\nImportar:")
print("  from datetime import datetime, date, time, timedelta")

print("\nCrear fechas:")
print("  datetime.now() - Fecha y hora actual")
print("  datetime(2024, 1, 15) - Fecha específica")
print("  date(2024, 1, 15) - Solo fecha")
print("  time(14, 30) - Solo hora")

print("\nFormatear:")
print("  fecha.strftime('%Y-%m-%d') - Fecha a texto")
print("  datetime.strptime(texto, formato) - Texto a fecha")

print("\nOperaciones:")
print("  fecha1 - fecha2 - Diferencia (timedelta)")
print("  fecha + timedelta(days=7) - Sumar tiempo")
print("  fecha - timedelta(days=7) - Restar tiempo")

print("\nComponentes:")
print("  fecha.year, fecha.month, fecha.day")
print("  fecha.hour, fecha.minute, fecha.second")

print("\nComparar:")
print("  fecha1 < fecha2")
print("  fecha1 > fecha2")
print("  fecha1 == fecha2")

print("\nFormatos comunes:")
print("  %Y-%m-%d - 2024-01-15")
print("  %d/%m/%Y - 15/01/2024")
print("  %H:%M:%S - 14:30:00")

print("\n" + "=" * 50)
