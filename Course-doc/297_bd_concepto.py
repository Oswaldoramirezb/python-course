"""
BASES DE DATOS: CONCEPTO
========================
Trabajar con bases de datos en Python
"""

print("=" * 50)
print("CONCEPTO DE BASES DE DATOS")
print("=" * 50)

print("\nBases de datos:")
print("  - Almacenamiento estructurado de datos")
print("  - SQL y NoSQL")
print("  - Múltiples bibliotecas disponibles")

print("\nTipos:")
print("  SQL - Estructurado (SQLite, PostgreSQL, MySQL)")
print("  NoSQL - No estructurado (MongoDB, Redis)")

print("\nBibliotecas principales:")
print("  sqlite3 - SQLite (incluido en Python)")
print("  psycopg2 - PostgreSQL")
print("  pymysql - MySQL")
print("  sqlalchemy - ORM (Object-Relational Mapping)")
print("  pymongo - MongoDB")

print("\nOperaciones básicas:")
print("  CREATE - Crear tablas")
print("  INSERT - Insertar datos")
print("  SELECT - Consultar datos")
print("  UPDATE - Actualizar datos")
print("  DELETE - Eliminar datos")

print("\nEjemplo SQLite:")
print("  import sqlite3")
print("  conn = sqlite3.connect('base.db')")
print("  cursor = conn.cursor()")
print("  cursor.execute('SELECT * FROM tabla')")
print("  resultados = cursor.fetchall()")

print("\nVentajas:")
print("  ✅ Persistencia de datos")
print("  ✅ Consultas eficientes")
print("  ✅ Integridad de datos")
print("  ✅ Escalabilidad")

print("\n" + "=" * 50)
