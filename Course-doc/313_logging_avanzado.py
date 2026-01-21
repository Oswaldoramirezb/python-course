"""
LOGGING: AVANZADO
=================
Configuración avanzada de logging
"""

print("=" * 50)
print("LOGGING AVANZADO")
print("=" * 50)

import logging

# Configuración avanzada
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='a'
)

print("\nConfiguración avanzada:")
print("  logging.basicConfig(")
print("      level=logging.DEBUG,")
print("      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',")
print("      filename='app.log',")
print("      filemode='a'")
print("  )")

logger = logging.getLogger(__name__)

# Logging a archivo y consola
print("\nLogging a archivo y consola:")
print("  - filename='app.log' - Guardar en archivo")
print("  - filemode='a' - Modo append")
print("  - format - Formato personalizado")

logger.info("Mensaje guardado en archivo")

# Múltiples handlers
print("\nMúltiples handlers:")
file_handler = logging.FileHandler('app.log')
console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger2 = logging.getLogger('mi_app')
logger2.addHandler(file_handler)
logger2.addHandler(console_handler)
logger2.setLevel(logging.DEBUG)

logger2.info("Mensaje con múltiples handlers")

print("\nFormato personalizado:")
print("  %(asctime)s - Fecha y hora")
print("  %(name)s - Nombre del logger")
print("  %(levelname)s - Nivel")
print("  %(message)s - Mensaje")
print("  %(filename)s - Archivo")
print("  %(lineno)d - Línea")

print("\nRotación de archivos:")
print("  from logging.handlers import RotatingFileHandler")
print("  handler = RotatingFileHandler('app.log', maxBytes=1024, backupCount=3)")

print("\n" + "=" * 50)
