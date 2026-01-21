"""
LOGGING: BÁSICO
===============
Sistema de logging de Python
"""

print("=" * 50)
print("LOGGING BÁSICO")
print("=" * 50)

import logging

# Configuración básica
logging.basicConfig(level=logging.INFO)

print("\nConfiguración básica:")
print("  import logging")
print("  logging.basicConfig(level=logging.INFO)")

# Crear logger
logger = logging.getLogger(__name__)

print("\nNiveles de logging:")
print("  DEBUG - Información detallada")
print("  INFO - Información general")
print("  WARNING - Advertencias")
print("  ERROR - Errores")
print("  CRITICAL - Errores críticos")

# Ejemplos de logging
logger.debug("Este es un mensaje DEBUG")
logger.info("Este es un mensaje INFO")
logger.warning("Este es un mensaje WARNING")
logger.error("Este es un mensaje ERROR")
logger.critical("Este es un mensaje CRITICAL")

print("\nUsar logger:")
print("  logger = logging.getLogger(__name__)")
print("  logger.info('Mensaje')")
print("  logger.error('Error')")

# Logging con formato
print("\nLogging con formato:")
logger.info("Usuario %s realizó acción", "Juan")
logger.info(f"Valor calculado: {10 + 5}")

print("\nVentajas sobre print():")
print("  ✅ Niveles de importancia")
print("  ✅ Configurable")
print("  ✅ Puede guardar en archivo")
print("  ✅ Formato estructurado")
print("  ✅ Fácil de desactivar")

print("\n" + "=" * 50)
