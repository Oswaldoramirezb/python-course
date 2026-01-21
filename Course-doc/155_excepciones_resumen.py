"""
RESUMEN: EXCEPCIONES
====================
Todas las operaciones con excepciones
"""

print("=" * 50)
print("RESUMEN - EXCEPCIONES")
print("=" * 50)

print("\nEstructura básica:")
print("  try:")
print("      código_que_puede_fallar()")
print("  except TipoError:")
print("      manejar_error()")
print("  else:")
print("      código_si_no_hay_error()")
print("  finally:")
print("      código_siempre_se_ejecuta()")

print("\nTipos comunes:")
print("  ZeroDivisionError - División por cero")
print("  ValueError - Valor incorrecto")
print("  TypeError - Tipo incorrecto")
print("  IndexError - Índice fuera de rango")
print("  KeyError - Clave no existe")
print("  FileNotFoundError - Archivo no encontrado")

print("\nOperaciones:")
print("  raise - Lanzar excepción")
print("  assert - Afirmación")
print("  Excepciones personalizadas - Crear tus propias")

print("\nBuenas prácticas:")
print("  ✅ Ser específico con tipos")
print("  ✅ No silenciar errores")
print("  ✅ Usar finally para limpiar")
print("  ✅ Mensajes de error útiles")

print("\n" + "=" * 50)
