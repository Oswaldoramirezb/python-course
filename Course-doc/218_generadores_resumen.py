"""
RESUMEN: GENERADORES
====================
Todas las operaciones con generadores
"""

print("=" * 50)
print("RESUMEN - GENERADORES")
print("=" * 50)

print("\nConcepto:")
print("  - Función que retorna iterador")
print("  - Usa 'yield' en lugar de 'return'")
print("  - Genera valores uno a uno")

print("\nCrear generador:")
print("  def generador():")
print("      yield valor")
print("")
print("  O con expresión:")
print("  (x**2 for x in range(5))")

print("\nUsar generador:")
print("  for valor in generador():")
print("      print(valor)")
print("")
print("  O con next():")
print("  next(generador)")

print("\nOperaciones:")
print("  - next() - Obtener siguiente valor")
print("  - send() - Enviar valor al generador")
print("  - close() - Cerrar generador")

print("\nVentajas:")
print("  ✅ Eficiencia de memoria")
print("  ✅ Generación bajo demanda")
print("  ✅ Puede ser infinito")

print("\nComparación:")
print("  Lista: [x**2 for x in range(5)]  # Todos en memoria")
print("  Generador: (x**2 for x in range(5))  # Uno a uno")

print("\n" + "=" * 50)
