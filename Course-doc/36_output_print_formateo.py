"""
OUTPUT: PRINT CON FORMATEO
==========================
Formatear números y texto al imprimir
"""

print("=" * 50)
print("PRINT CON FORMATEO")
print("=" * 50)

# Formatear números decimales
precio = 19.99
print(f"\nFormatear decimales:")
print(f"Precio: ${precio:.2f}")  # 2 decimales

# Formatear enteros con ceros
numero = 5
print(f"\nFormatear con ceros:")
print(f"Número: {numero:03d}")  # 005

# Formatear texto
texto = "Python"
print(f"\nFormatear texto:")
print(f"{texto:>10}")  # Alineado a la derecha
print(f"{texto:<10}")  # Alineado a la izquierda
print(f"{texto:^10}")  # Centrado

print("\n" + "=" * 50)
