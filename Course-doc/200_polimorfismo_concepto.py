"""
POLIMORFISMO: CONCEPTO
======================
Un mismo método puede comportarse diferente según el objeto
"""

print("=" * 50)
print("CONCEPTO DE POLIMORFISMO")
print("=" * 50)

print("\nPolimorfismo significa:")
print("  - 'Muchas formas'")
print("  - Mismo método, diferentes comportamientos")
print("  - Depende del tipo de objeto")

print("\nEjemplo:")
print("  Animal.hacer_sonido()")
print("  - Perro.hacer_sonido() → 'Guau'")
print("  - Gato.hacer_sonido() → 'Miau'")
print("  - Pato.hacer_sonido() → 'Cuac'")

print("\nTipos de polimorfismo:")
print("  - Polimorfismo de métodos (override)")
print("  - Duck typing")
print("  - Polimorfismo con interfaces")

print("\nVentajas:")
print("  ✅ Código más flexible")
print("  ✅ Mismo código para diferentes tipos")
print("  ✅ Extensibilidad")

print("\nEjemplo en código:")
print("  def hacer_ruido(animal):")
print("      animal.hacer_sonido()")
print("")
print("  hacer_ruido(perro)  # 'Guau'")
print("  hacer_ruido(gato)  # 'Miau'")

print("\n" + "=" * 50)
