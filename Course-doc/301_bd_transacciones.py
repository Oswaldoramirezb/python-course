"""
BASES DE DATOS: TRANSACCIONES
=============================
Manejo de transacciones
"""

print("=" * 50)
print("TRANSACCIONES")
print("=" * 50)

import sqlite3
import os

db_file = "ejemplo_trans.db"
if os.path.exists(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute("CREATE TABLE cuentas (id INTEGER PRIMARY KEY, saldo REAL)")
cursor.execute("INSERT INTO cuentas VALUES (1, 1000.0)")
cursor.execute("INSERT INTO cuentas VALUES (2, 500.0)")
conn.commit()

print("\nTransacciones:")
print("  - Operaciones atómicas (todo o nada)")
print("  - commit() - Confirmar cambios")
print("  - rollback() - Deshacer cambios")

# Transacción exitosa
print("\nTransacción exitosa:")
try:
    cursor.execute("UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1")
    cursor.execute("UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2")
    conn.commit()
    print("  ✅ Transacción completada")
except Exception as e:
    conn.rollback()
    print(f"  ❌ Error: {e}")

# Transacción con error (rollback)
print("\nTransacción con error (rollback):")
try:
    cursor.execute("UPDATE cuentas SET saldo = saldo - 200 WHERE id = 1")
    cursor.execute("UPDATE cuentas SET saldo = saldo + 200 WHERE id = 999")  # Error
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"  ❌ Error: {e}")
    print("  ✅ Cambios deshechos (rollback)")

# Verificar saldos
cursor.execute("SELECT * FROM cuentas")
print("\nSaldos finales:")
for row in cursor.fetchall():
    print(f"  {row}")

conn.close()

print("\nVentajas:")
print("  ✅ Integridad de datos")
print("  ✅ Operaciones atómicas")
print("  ✅ Recuperación de errores")

print("\n" + "=" * 50)
