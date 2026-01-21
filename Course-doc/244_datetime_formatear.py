"""
DATETIME: FORMATEAR
===================
Formatear fechas y horas como texto
"""

print("=" * 50)
print("FORMATEAR FECHAS")
print("=" * 50)

from datetime import datetime

ahora = datetime.now()
print(f"\nFecha actual: {ahora}")

# strftime - fecha a texto
print("\nstrftime (fecha a texto):")
print(f"  ahora.strftime('%Y-%m-%d') = {ahora.strftime('%Y-%m-%d')}")
print(f"  ahora.strftime('%d/%m/%Y') = {ahora.strftime('%d/%m/%Y')}")
print(f"  ahora.strftime('%H:%M:%S') = {ahora.strftime('%H:%M:%S')}")
print(f"  ahora.strftime('%A, %d de %B de %Y') = {ahora.strftime('%A, %d de %B de %Y')}")

# strptime - texto a fecha
print("\nstrptime (texto a fecha):")
texto_fecha = "2024-01-15 14:30:00"
fecha = datetime.strptime(texto_fecha, "%Y-%m-%d %H:%M:%S")
print(f"  datetime.strptime('{texto_fecha}', '%Y-%m-%d %H:%M:%S') = {fecha}")

# Formatos comunes
print("\nFormatos comunes:")
print("  %Y - Año (4 dígitos)")
print("  %m - Mes (01-12)")
print("  %d - Día (01-31)")
print("  %H - Hora (00-23)")
print("  %M - Minuto (00-59)")
print("  %S - Segundo (00-59)")

print("\n" + "=" * 50)
