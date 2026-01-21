"""
DEBUGGING: PDB
==============
Python Debugger interactivo
"""

print("=" * 50)
print("PDB - PYTHON DEBUGGER")
print("=" * 50)

print("\nPDB:")
print("  - Debugger interactivo de Python")
print("  - Incluido en la biblioteca estándar")
print("  - Permite inspeccionar código en ejecución")

print("\nUsar pdb:")
print("  import pdb")
print("  pdb.set_trace()  # Punto de interrupción")

print("\nComandos principales:")
print("  n (next) - Siguiente línea")
print("  s (step) - Entrar en función")
print("  c (continue) - Continuar")
print("  l (list) - Mostrar código")
print("  p variable - Imprimir variable")
print("  pp variable - Imprimir bonito")
print("  q (quit) - Salir")

print("\nEjemplo:")
print("  def dividir(a, b):")
print("      import pdb; pdb.set_trace()")
print("      return a / b")
print("")
print("  resultado = dividir(10, 2)")

print("\nBreakpoint condicional:")
print("  if condicion:")
print("      import pdb; pdb.set_trace()")

print("\nPost-mortem debugging:")
print("  python -m pdb script.py")
print("  - Ejecuta script en modo debugger")

print("\nVentajas:")
print("  ✅ Interactivo")
print("  ✅ Inspeccionar variables")
print("  ✅ Controlar ejecución")
print("  ✅ Incluido en Python")

print("\nAlternativas modernas:")
print("  - IDE debuggers (VS Code, PyCharm)")
print("  - ipdb (mejorado)")
print("  - pudb (interfaz visual)")

print("\n" + "=" * 50)
