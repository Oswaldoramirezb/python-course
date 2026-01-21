"""
RESUMEN: BASES DE DATOS
=======================
Todas las operaciones con bases de datos
"""

print("=" * 50)
print("RESUMEN - BASES DE DATOS")
print("=" * 50)

print("\nSQLite (incluido):")
print("  import sqlite3")
print("  conn = sqlite3.connect('base.db')")
print("  cursor = conn.cursor()")
print("  cursor.execute('SQL')")
print("  conn.commit()")
print("  conn.close()")

print("\nOperaciones SQL:")
print("  CREATE TABLE - Crear tabla")
print("  INSERT - Insertar datos")
print("  SELECT - Consultar")
print("  UPDATE - Actualizar")
print("  DELETE - Eliminar")

print("\nConsultas:")
print("  WHERE - Filtrar")
print("  ORDER BY - Ordenar")
print("  GROUP BY - Agrupar")
print("  JOIN - Combinar tablas")

print("\nTransacciones:")
print("  conn.commit() - Confirmar")
print("  conn.rollback() - Deshacer")

print("\nORM (SQLAlchemy):")
print("  - Trabajar con objetos")
print("  - Menos SQL manual")
print("  - Compatible con múltiples BD")

print("\nBibliotecas:")
print("  sqlite3 - SQLite")
print("  psycopg2 - PostgreSQL")
print("  pymysql - MySQL")
print("  sqlalchemy - ORM")
print("  pymongo - MongoDB")

print("\nVentajas:")
print("  ✅ Persistencia")
print("  ✅ Consultas eficientes")
print("  ✅ Integridad de datos")
print("  ✅ Escalabilidad")

print("\n" + "=" * 50)
