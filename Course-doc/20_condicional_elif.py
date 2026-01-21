"""
CONDICIONAL: ELIF
=================
Permite verificar múltiples condiciones
"""

print("=" * 50)
print("IF-ELIF-ELSE")
print("=" * 50)

nota = 85
print(f"\nnota = {nota}")

if nota >= 90:
    print("  ⭐ Excelente (A)")
elif nota >= 80:
    print("  👍 Muy bien (B)")
elif nota >= 70:
    print("  ✅ Bien (C)")
else:
    print("  ⚠️  Necesitas mejorar")

print("\n--- Probando con otra nota ---")
nota = 95
print(f"nota = {nota}")

if nota >= 90:
    print("  ⭐ Excelente (A)")
elif nota >= 80:
    print("  👍 Muy bien (B)")
elif nota >= 70:
    print("  ✅ Bien (C)")
else:
    print("  ⚠️  Necesitas mejorar")

print("\n" + "=" * 50)
