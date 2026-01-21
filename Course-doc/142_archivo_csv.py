"""
ARCHIVO: CSV
============
Trabajar con archivos CSV
"""

print("=" * 50)
print("ARCHIVOS CSV")
print("=" * 50)

import csv

# Escribir CSV
encabezados = ["Nombre", "Edad", "Ciudad"]
datos = [
    ["Ana", 25, "Barcelona"],
    ["Luis", 30, "Madrid"],
    ["María", 28, "Valencia"]
]

print("\nEscribir CSV:")
with open("personas.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(encabezados)
    escritor.writerows(datos)
    print("  ✅ Datos escritos en personas.csv")

# Leer CSV
print("\nLeer CSV:")
with open("personas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    encabezados_leidos = next(lector)
    print(f"  Encabezados: {encabezados_leidos}")
    for fila in lector:
        print(f"  {fila}")

# Leer como diccionario
print("\nLeer como diccionario:")
with open("personas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for persona in lector:
        print(f"  {persona}")

print("\n" + "=" * 50)
