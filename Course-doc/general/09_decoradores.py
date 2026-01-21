"""
DECORADORES - Funciones de Orden Superior
==========================================
"""

# ========== FUNCIONES COMO OBJETOS ==========

def saludar():
    return "Hola"

# Las funciones son objetos de primera clase
mi_funcion = saludar
print(mi_funcion())

# ========== DECORADOR BÁSICO ==========

def mi_decorador(func):
    """Decorador simple que agrega funcionalidad"""
    def wrapper():
        print("Antes de ejecutar la función")
        resultado = func()
        print("Después de ejecutar la función")
        return resultado
    return wrapper

@mi_decorador
def decir_hola():
    print("¡Hola!")

print("\n=== DECORADOR BÁSICO ===")
decir_hola()

# ========== DECORADOR CON ARGUMENTOS ==========

def decorador_con_args(func):
    """Decorador que maneja funciones con argumentos"""
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con argumentos: {args}, {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@decorador_con_args
def sumar(a, b):
    return a + b

print("\n=== DECORADOR CON ARGUMENTOS ===")
sumar(5, 3)

# ========== PRESERVAR METADATOS CON functools.wraps ==========

from functools import wraps

def decorador_preservar_metadata(func):
    """Decorador que preserva los metadatos de la función original"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper interno"""
        return func(*args, **kwargs)
    return wrapper

@decorador_preservar_metadata
def multiplicar(x, y):
    """Multiplica dos números"""
    return x * y

print("\n=== PRESERVAR METADATOS ===")
print(f"Nombre: {multiplicar.__name__}")
print(f"Docstring: {multiplicar.__doc__}")

# ========== DECORADOR CON PARÁMETROS ==========

def repetir(veces):
    """Decorador con parámetros"""
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(veces):
                print(f"Ejecución {i+1}: {func(*args, **kwargs)}")
        return wrapper
    return decorador

@repetir(3)
def saludar_nombre(nombre):
    return f"¡Hola, {nombre}!"

print("\n=== DECORADOR CON PARÁMETROS ===")
saludar_nombre("Juan")

# ========== DECORADORES ÚTILES ==========

# Decorador para medir tiempo de ejecución
import time

def medir_tiempo(func):
    """Decorador que mide el tiempo de ejecución"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def operacion_lenta():
    """Simula una operación que toma tiempo"""
    time.sleep(0.1)
    return "Operación completada"

print("\n=== MEDIR TIEMPO ===")
operacion_lenta()

# Decorador para validar argumentos
def validar_positivos(func):
    """Valida que los argumentos sean positivos"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Los argumentos deben ser positivos")
        return func(*args, **kwargs)
    return wrapper

@validar_positivos
def calcular_area_rectangulo(ancho, alto):
    return ancho * alto

print("\n=== VALIDACIÓN ===")
try:
    print(f"Área: {calcular_area_rectangulo(5, 3)}")
    calcular_area_rectangulo(-5, 3)
except ValueError as e:
    print(f"Error: {e}")

# Decorador para cachear resultados
def cachear(func):
    """Decorador que cachea los resultados"""
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        clave = str(args) + str(kwargs)
        if clave not in cache:
            cache[clave] = func(*args, **kwargs)
        return cache[clave]
    return wrapper

@cachear
def fibonacci(n):
    """Calcula Fibonacci (versión ineficiente sin cache)"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n=== CACHE ===")
import time
inicio = time.time()
resultado = fibonacci(30)
fin = time.time()
print(f"Fibonacci(30) = {resultado} (tardó {fin-inicio:.4f}s)")

# Decorador para logging
def log(func):
    """Decorador que registra llamadas a funciones"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} retornó: {resultado}")
        return resultado
    return wrapper

@log
def dividir(a, b):
    return a / b

print("\n=== LOGGING ===")
dividir(10, 2)

# ========== MÚLTIPLES DECORADORES ==========

def decorador1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorador 1: antes")
        resultado = func(*args, **kwargs)
        print("Decorador 1: después")
        return resultado
    return wrapper

def decorador2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorador 2: antes")
        resultado = func(*args, **kwargs)
        print("Decorador 2: después")
        return resultado
    return wrapper

@decorador1
@decorador2
def mi_funcion():
    print("Función ejecutándose")

print("\n=== MÚLTIPLES DECORADORES ===")
mi_funcion()

# ========== DECORADOR DE CLASE ==========

def decorador_clase(cls):
    """Decorador aplicado a una clase"""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
        
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    
    return Wrapper

@decorador_clase
class MiClase:
    def __init__(self, valor):
        self.valor = valor
    
    def mostrar(self):
        return f"Valor: {self.valor}"

print("\n=== DECORADOR DE CLASE ===")
obj = MiClase(42)
print(obj.mostrar())

# ========== DECORADORES DE CLASE (Python 3.9+) ==========

class ContadorLlamadas:
    """Decorador de clase que cuenta llamadas"""
    def __init__(self, func):
        self.func = func
        self.contador = 0
        wraps(func)(self)
    
    def __call__(self, *args, **kwargs):
        self.contador += 1
        print(f"{self.func.__name__} ha sido llamada {self.contador} veces")
        return self.func(*args, **kwargs)

@ContadorLlamadas
def saludar():
    return "Hola"

print("\n=== DECORADOR DE CLASE ===")
saludar()
saludar()
saludar()

# ========== EJEMPLO PRÁCTICO: SISTEMA DE AUTENTICACIÓN ==========

usuarios_autenticados = {"admin", "usuario1"}

def requiere_autenticacion(func):
    """Decorador que requiere autenticación"""
    @wraps(func)
    def wrapper(usuario, *args, **kwargs):
        if usuario not in usuarios_autenticados:
            return f"Error: Usuario '{usuario}' no autenticado"
        return func(usuario, *args, **kwargs)
    return wrapper

@requiere_autenticacion
def acceder_recurso(usuario, recurso):
    return f"Usuario {usuario} accedió a {recurso}"

print("\n=== AUTENTICACIÓN ===")
print(acceder_recurso("admin", "base_de_datos"))
print(acceder_recurso("invitado", "base_de_datos"))

# ========== EJEMPLO PRÁCTICO: RETRY (REINTENTOS) ==========

def reintentar(max_intentos=3, delay=1):
    """Decorador que reintenta una función si falla"""
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(max_intentos):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if intento == max_intentos - 1:
                        raise
                    print(f"Intento {intento + 1} falló: {e}. Reintentando...")
                    time.sleep(delay)
        return wrapper
    return decorador

@reintentar(max_intentos=3, delay=0.1)
def operacion_inestable():
    """Simula una operación que puede fallar"""
    import random
    if random.random() < 0.7:
        raise Exception("Error temporal")
    return "Operación exitosa"

print("\n=== REINTENTOS ===")
try:
    resultado = operacion_inestable()
    print(resultado)
except Exception as e:
    print(f"Falló después de todos los intentos: {e}")
