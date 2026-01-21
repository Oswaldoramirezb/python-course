"""
CONDICIONALES: ANIDADOS
=======================
Condicionales dentro de otros condicionales
"""

print("=" * 50)
print("CONDICIONALES ANIDADOS")
print("=" * 50)

# Ejemplo práctico
usuario_activo = True
saldo = 1000

print(f"\nEjemplo:")
print(f"  usuario_activo = {usuario_activo}")
print(f"  saldo = ${saldo}")

if usuario_activo:
    print("  ✅ Usuario activo")
    if saldo > 0:
        print("  💰 Puedes realizar transacciones")
        if saldo >= 1000:
            print("  🎉 Tienes un saldo alto")
    else:
        print("  ⚠️  Tu cuenta está sin saldo")
else:
    print("  ❌ Usuario inactivo")

print("\n--- Cambiando valores ---")
saldo = 0
print(f"\n  saldo = ${saldo}")
if usuario_activo:
    if saldo > 0:
        print("  💰 Puedes realizar transacciones")
    else:
        print("  ⚠️  Tu cuenta está sin saldo")

print("\n" + "=" * 50)
