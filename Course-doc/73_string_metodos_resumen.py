"""
RESUMEN: MÉTODOS DE STRING
===========================
Todos los métodos importantes de cadenas
"""

print("=" * 50)
print("RESUMEN - MÉTODOS DE STRING")
print("=" * 50)

texto = "  Python es Genial  "

print(f"\nTexto ejemplo: '{texto}'")
print(f"\nMétodos principales:")
print(f"  upper()      → '{texto.upper()}'")
print(f"  lower()      → '{texto.lower()}'")
print(f"  strip()      → '{texto.strip()}'")
print(f"  split()      → {texto.strip().split()}")
print(f"  replace()    → '{texto.replace('Genial', 'Fantástico')}'")
print(f"  find()       → {texto.find('Python')}")
print(f"  count()      → {texto.count('e')}")
print(f"  startswith() → {texto.startswith('Python')}")
print(f"  endswith()   → {texto.endswith('Genial')}")

print("\n" + "=" * 50)
