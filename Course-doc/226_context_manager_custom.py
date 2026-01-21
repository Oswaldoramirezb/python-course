"""
CONTEXT MANAGER: PERSONALIZADO
==============================
Crear tu propio context manager
"""

print("=" * 50)
print("CONTEXT MANAGER PERSONALIZADO")
print("=" * 50)

# Context manager como clase
class ArchivoSeguro:
    """Context manager para manejo seguro de archivos"""
    def __init__(self, nombre_archivo, modo='r'):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
    
    def __enter__(self):
        """Se ejecuta al entrar al bloque with"""
        self.archivo = open(self.nombre_archivo, self.modo, encoding='utf-8')
        print(f"  ✅ Archivo '{self.nombre_archivo}' abierto")
        return self.archivo
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
        """Se ejecuta al salir del bloque with"""
        if self.archivo:
            self.archivo.close()
            print(f"  ✅ Archivo '{self.nombre_archivo}' cerrado")
        return False  # No suprime excepciones

print("\nContext manager personalizado:")
print("  class ArchivoSeguro:")
print("      def __enter__(self):")
print("          # Abrir recurso")
print("          return self.archivo")
print("")
print("      def __exit__(self, tipo, valor, traceback):")
print("          # Cerrar recurso")

# Usar context manager
with open("ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("Test")

with ArchivoSeguro("ejemplo.txt", 'r') as archivo:
    contenido = archivo.read()
    print(f"\n  Contenido: {contenido[:20]}...")

print("\n" + "=" * 50)
