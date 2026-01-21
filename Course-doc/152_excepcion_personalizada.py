"""
EXCEPCIÓN: PERSONALIZADA
========================
Crear tus propias excepciones
"""

print("=" * 50)
print("EXCEPCIONES PERSONALIZADAS")
print("=" * 50)

# Excepción personalizada básica
class EdadInvalidaError(Exception):
    """Excepción personalizada para edad inválida"""
    pass

print("\nEjemplo 1 - Excepción personalizada simple:")
def validar_edad(edad):
    if edad < 0 or edad > 150:
        raise EdadInvalidaError(f"Edad {edad} no es válida")
    return True

try:
    validar_edad(200)
except EdadInvalidaError as e:
    print(f"  ✅ Error personalizado capturado: {e}")

# Excepción con más información
print("\nEjemplo 2 - Excepción con información:")
class ErrorValidacion(Exception):
    def __init__(self, mensaje, codigo_error):
        self.mensaje = mensaje
        self.codigo_error = codigo_error
        super().__init__(self.mensaje)
    
    def __str__(self):
        return f"[{self.codigo_error}] {self.mensaje}"

def validar_email(email):
    if '@' not in email:
        raise ErrorValidacion("Email inválido: falta @", "ERR001")
    return True

try:
    validar_email("email_sin_arroba")
except ErrorValidacion as e:
    print(f"  ✅ Error personalizado: {e}")

print("\n" + "=" * 50)
