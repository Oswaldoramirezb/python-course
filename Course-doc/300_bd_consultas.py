"""
BASES DE DATOS: CONSULTAS
=========================
Consultas SQL avanzadas
"""

print("=" * 50)
print("CONSULTAS SQL")
print("=" * 50)

import sqlite3
import os

# Crear base de datos de ejemplo
db_file = "ejemplo_consultas.db"
if os.path.exists(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Crear tabla
cursor.execute("""
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        precio REAL,
        categoria TEXT
    )
""")

# Insertar datos
productos = [
    ("Laptop", 999.99, "Electrónica"),
    ("Mouse", 29.99, "Electrónica"),
    ("Silla", 149.99, "Muebles"),
    ("Mesa", 299.99, "Muebles")
]
cursor.executemany("INSERT INTO productos VALUES (?, ?, ?, ?)", 
                   [(i+1, *p) for i, p in enumerate(productos)])
conn.commit()

print("\nConsultas básicas:")

# SELECT con WHERE
cursor.execute("SELECT * FROM productos WHERE precio > 100")
print("\n1. WHERE:")
print("  SELECT * FROM productos WHERE precio > 100")
for row in cursor.fetchall():
    print(f"    {row}")

# SELECT con ORDER BY
cursor.execute("SELECT * FROM productos ORDER BY precio DESC")
print("\n2. ORDER BY:")
print("  SELECT * FROM productos ORDER BY precio DESC")
for row in cursor.fetchall():
    print(f"    {row}")

# SELECT con GROUP BY
cursor.execute("SELECT categoria, COUNT(*) FROM productos GROUP BY categoria")
print("\n3. GROUP BY:")
print("  SELECT categoria, COUNT(*) FROM productos GROUP BY categoria")
for row in cursor.fetchall():
    print(f"    {row}")

# SELECT con JOIN (si hubiera otra tabla)
print("\n4. JOIN:")
print("  SELECT * FROM tabla1 JOIN tabla2 ON tabla1.id = tabla2.id")

conn.close()

print("\n" + "=" * 50)
