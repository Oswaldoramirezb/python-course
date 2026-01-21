"""
BASES DE DATOS: SQLITE
======================
Trabajar con SQLite
"""

print("=" * 50)
print("SQLITE")
print("=" * 50)

import sqlite3
import os

# Conectar a base de datos
db_file = "ejemplo.db"
if os.path.exists(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

print("\nConectar:")
print("  conn = sqlite3.connect('base.db')")
print("  cursor = conn.cursor()")

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER
    )
""")
conn.commit()

print("\nCrear tabla:")
print("  cursor.execute('CREATE TABLE usuarios ...')")
print("  conn.commit()")

# Insertar datos
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan", 30))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("María", 25))
conn.commit()

print("\nInsertar datos:")
print("  cursor.execute('INSERT INTO usuarios ...', ('Juan', 30))")
print("  conn.commit()")

# Consultar datos
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()

print("\nConsultar datos:")
print("  cursor.execute('SELECT * FROM usuarios')")
print("  resultados = cursor.fetchall()")
print(f"  {resultados}")

# Consultar con fetchone
cursor.execute("SELECT * FROM usuarios WHERE edad > 25")
resultado = cursor.fetchone()
print(f"\nConsultar uno:")
print(f"  cursor.fetchone() = {resultado}")

# Actualizar
cursor.execute("UPDATE usuarios SET edad = 31 WHERE nombre = 'Juan'")
conn.commit()

print("\nActualizar:")
print("  cursor.execute('UPDATE usuarios SET edad = 31 ...')")
print("  conn.commit()")

# Cerrar conexión
conn.close()
print("\nCerrar:")
print("  conn.close()")

print("\n" + "=" * 50)
