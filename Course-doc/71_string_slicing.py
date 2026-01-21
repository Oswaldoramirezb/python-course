"""
STRING: SLICING
===============
Extraer partes de una cadena
"""

print("=" * 50)
print("STRING SLICING")
print("=" * 50)

# Slicing básico
texto = "Python"
print(f"\nTexto: '{texto}'")

print(f"  texto[0] = '{texto[0]}' (primer carácter)")
print(f"  texto[-1] = '{texto[-1]}' (último carácter)")
print(f"  texto[1:4] = '{texto[1:4]}' (del índice 1 al 3)")
print(f"  texto[:3] = '{texto[:3]}' (desde inicio hasta 2)")
print(f"  texto[3:] = '{texto[3:]}' (desde índice 3 hasta final)")
print(f"  texto[::-1] = '{texto[::-1]}' (invertido)")

# Slicing con paso
print(f"\nCon paso:")
print(f"  texto[::2] = '{texto[::2]}' (cada 2 caracteres)")

print("\n" + "=" * 50)
