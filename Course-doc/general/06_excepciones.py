"""
MANEJO DE EXCEPCIONES - Try, Except, Finally
=============================================
"""

# ========== EXCEPCIONES BÁSICAS ==========

# Try-except básico
def dividir(a, b):
    """Divide dos números con manejo de errores"""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"

print(f"10 / 2 = {dividir(10, 2)}")
print(f"10 / 0 = {dividir(10, 0)}")

# Múltiples excepciones
def convertir_a_entero(valor):
    """Convierte un valor a entero"""
    try:
        numero = int(valor)
        return numero
    except ValueError:
        return f"Error: '{valor}' no es un número válido"
    except TypeError:
        return "Error: Tipo de dato no soportado"

print(f"Convertir '123': {convertir_a_entero('123')}")
print(f"Convertir 'abc': {convertir_a_entero('abc')}")

# Excepción genérica
def acceder_lista(lista, indice):
    """Accede a un elemento de una lista"""
    try:
        return lista[indice]
    except IndexError:
        return f"Error: Índice {indice} fuera de rango"
    except TypeError:
        return "Error: El primer argumento debe ser una lista"

lista = [1, 2, 3]
print(f"Elemento en índice 1: {acceder_lista(lista, 1)}")
print(f"Elemento en índice 10: {acceder_lista(lista, 10)}")

# ========== TRY-EXCEPT-ELSE ==========

def leer_archivo(nombre_archivo):
    """Lee un archivo con manejo de excepciones"""
    try:
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe")
    else:
        # Este bloque se ejecuta si NO hubo excepción
        contenido = archivo.read()
        archivo.close()
        print("Archivo leído correctamente")
        return contenido
    finally:
        # Este bloque siempre se ejecuta
        print("Operación de lectura finalizada")

# ========== TRY-EXCEPT-FINALLY ==========

def operacion_archivo(nombre_archivo):
    """Operación con archivo usando finally"""
    archivo = None
    try:
        archivo = open(nombre_archivo, 'w', encoding='utf-8')
        archivo.write("Contenido de prueba")
    except IOError as e:
        print(f"Error de E/S: {e}")
    finally:
        # Siempre se ejecuta, incluso si hay excepción
        if archivo:
            archivo.close()
            print("Archivo cerrado")

# ========== CAPTURAR INFORMACIÓN DE LA EXCEPCIÓN ==========

def dividir_detallado(a, b):
    """Divide con información detallada del error"""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError as e:
        print(f"Tipo de excepción: {type(e).__name__}")
        print(f"Mensaje: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")
        return None

dividir_detallado(10, 0)

# ========== LEVANTAR EXCEPCIONES (RAISE) ==========

def validar_edad(edad):
    """Valida que la edad sea válida"""
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 150:
        raise ValueError("La edad no puede ser mayor a 150")
    return True

try:
    validar_edad(-5)
except ValueError as e:
    print(f"Error de validación: {e}")

# Crear excepciones personalizadas
class EdadInvalidaError(Exception):
    """Excepción personalizada para edad inválida"""
    pass

def validar_edad_personalizada(edad):
    """Valida edad con excepción personalizada"""
    if edad < 0 or edad > 150:
        raise EdadInvalidaError(f"Edad {edad} no es válida")
    return True

try:
    validar_edad_personalizada(200)
except EdadInvalidaError as e:
    print(f"Error personalizado: {e}")

# ========== EXCEPCIONES CON MÁS INFORMACIÓN ==========

class ErrorValidacion(Exception):
    """Excepción base para errores de validación"""
    def __init__(self, mensaje, codigo_error):
        self.mensaje = mensaje
        self.codigo_error = codigo_error
        super().__init__(self.mensaje)
    
    def __str__(self):
        return f"[{self.codigo_error}] {self.mensaje}"

def validar_email(email):
    """Valida formato de email"""
    if '@' not in email:
        raise ErrorValidacion("Email inválido: falta @", "ERR001")
    if '.' not in email.split('@')[1]:
        raise ErrorValidacion("Email inválido: dominio incorrecto", "ERR002")
    return True

try:
    validar_email("email_sin_arroba")
except ErrorValidacion as e:
    print(f"Error: {e}")

# ========== ASSERT (AFIRMACIONES) ==========

def calcular_promedio(notas):
    """Calcula el promedio de notas"""
    assert len(notas) > 0, "La lista de notas no puede estar vacía"
    assert all(0 <= nota <= 100 for nota in notas), "Las notas deben estar entre 0 y 100"
    return sum(notas) / len(notas)

try:
    promedio = calcular_promedio([85, 90, 78])
    print(f"Promedio: {promedio}")
except AssertionError as e:
    print(f"Error de aserción: {e}")

# ========== EJEMPLOS PRÁCTICOS ==========

# Manejo de excepciones en operaciones de archivo
def leer_configuracion(nombre_archivo):
    """Lee un archivo de configuración con manejo robusto"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo} no encontrado. Usando configuración por defecto.")
        return "configuracion_por_defecto"
    except PermissionError:
        print(f"Sin permisos para leer {nombre_archivo}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

# Validación de entrada del usuario
def obtener_numero():
    """Obtiene un número del usuario con validación"""
    while True:
        try:
            numero = float(input("Ingresa un número: "))
            return numero
        except ValueError:
            print("Error: Debes ingresar un número válido")
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario")
            return None

# Manejo de excepciones en operaciones de red (simulado)
def conectar_servidor(url):
    """Simula conexión a servidor"""
    import random
    try:
        # Simulación: 70% de probabilidad de éxito
        if random.random() < 0.7:
            return "Conexión exitosa"
        else:
            raise ConnectionError("No se pudo conectar al servidor")
    except ConnectionError as e:
        print(f"Error de conexión: {e}")
        # Reintentar lógica aquí
        return None

# Context manager con manejo de excepciones
class Recurso:
    """Recurso que necesita limpieza"""
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Recurso {nombre} inicializado")
    
    def usar(self):
        print(f"Usando recurso {self.nombre}")
        # Simular error ocasional
        import random
        if random.random() < 0.3:
            raise RuntimeError("Error al usar el recurso")
    
    def limpiar(self):
        print(f"Limpiando recurso {self.nombre}")

def usar_recurso_seguro(nombre):
    """Usa un recurso con manejo seguro"""
    recurso = Recurso(nombre)
    try:
        recurso.usar()
    except RuntimeError as e:
        print(f"Error: {e}")
    finally:
        recurso.limpiar()

# ========== TRACEBACK Y DEBUGGING ==========

import traceback

def funcion_problema():
    """Función que causa un error"""
    try:
        resultado = 10 / 0
    except:
        # Imprimir el traceback completo
        traceback.print_exc()
        # O guardar en string
        error_str = traceback.format_exc()
        return error_str

# ========== EJEMPLO COMPLETO: CALCULADORA ROBUSTA ==========

class Calculadora:
    """Calculadora con manejo robusto de errores"""
    
    @staticmethod
    def dividir(a, b):
        """Divide dos números"""
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Los argumentos deben ser números")
            if b == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            return a / b
        except (TypeError, ZeroDivisionError) as e:
            print(f"Error en división: {e}")
            return None
    
    @staticmethod
    def raiz_cuadrada(numero):
        """Calcula la raíz cuadrada"""
        try:
            if numero < 0:
                raise ValueError("No se puede calcular la raíz de un número negativo")
            import math
            return math.sqrt(numero)
        except ValueError as e:
            print(f"Error: {e}")
            return None

calc = Calculadora()
print(f"10 / 2 = {calc.dividir(10, 2)}")
print(f"10 / 0 = {calc.dividir(10, 0)}")
print(f"Raíz de 16 = {calc.raiz_cuadrada(16)}")
print(f"Raíz de -4 = {calc.raiz_cuadrada(-4)}")
