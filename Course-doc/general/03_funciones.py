"""
FUNCIONES - Definición, Parámetros y Alcance
============================================
"""

# ========== FUNCIONES BÁSICAS ==========

# Función simple sin parámetros
def saludar():
    """Función que imprime un saludo"""
    print("¡Hola, mundo!")

saludar()

# Función con parámetros
def saludar_persona(nombre):
    """Saluda a una persona específica"""
    print(f"¡Hola, {nombre}!")

saludar_persona("Juan")

# Función con múltiples parámetros
def sumar(a, b):
    """Suma dos números"""
    return a + b

resultado = sumar(5, 3)
print(f"5 + 3 = {resultado}")

# Función con valor de retorno
def calcular_promedio(num1, num2, num3):
    """Calcula el promedio de tres números"""
    promedio = (num1 + num2 + num3) / 3
    return promedio

promedio = calcular_promedio(10, 20, 30)
print(f"Promedio: {promedio}")

# ========== PARÁMETROS POR POSICIÓN Y POR NOMBRE ==========

def presentar(nombre, edad, ciudad):
    """Presenta a una persona"""
    print(f"{nombre}, {edad} años, de {ciudad}")

# Llamada por posición
presentar("María", 25, "Barcelona")

# Llamada por nombre (keyword arguments)
presentar(ciudad="Madrid", nombre="Pedro", edad=30)

# Combinación de ambos
presentar("Ana", edad=28, ciudad="Valencia")

# ========== PARÁMETROS POR DEFECTO ==========

def saludar_con_titulo(nombre, titulo="Sr./Sra."):
    """Saluda con un título opcional"""
    print(f"¡Hola, {titulo} {nombre}!")

saludar_con_titulo("García")
saludar_con_titulo("López", "Dr.")

# Múltiples parámetros por defecto
def crear_usuario(nombre, email, activo=True, rol="usuario"):
    """Crea un usuario con parámetros opcionales"""
    print(f"Usuario: {nombre}")
    print(f"Email: {email}")
    print(f"Activo: {activo}")
    print(f"Rol: {rol}")

crear_usuario("Juan", "juan@email.com")
crear_usuario("Admin", "admin@email.com", activo=True, rol="administrador")

# ========== ARGUMENTOS ARBITRARIOS: *args ==========

def sumar_numeros(*args):
    """Suma una cantidad variable de números"""
    total = 0
    for numero in args:
        total += numero
    return total

print(f"Suma: {sumar_numeros(1, 2, 3)}")
print(f"Suma: {sumar_numeros(10, 20, 30, 40, 50)}")

def mostrar_info(*args):
    """Muestra información variable"""
    for i, arg in enumerate(args):
        print(f"Argumento {i+1}: {arg}")

mostrar_info("Python", "es", "genial")

# ========== ARGUMENTOS ARBITRARIOS: **kwargs ==========

def crear_perfil(**kwargs):
    """Crea un perfil con argumentos de palabra clave"""
    print("Perfil creado:")
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

crear_perfil(nombre="Ana", edad=25, ciudad="Madrid", profesion="Ingeniera")

# Combinación de *args y **kwargs
def funcion_completa(*args, **kwargs):
    """Función que acepta ambos tipos de argumentos"""
    print("Argumentos posicionales:", args)
    print("Argumentos de palabra clave:", kwargs)

funcion_completa(1, 2, 3, nombre="Juan", edad=30)

# ========== FUNCIONES COMO OBJETOS ==========

def multiplicar(x, y):
    return x * y

# Asignar función a una variable
operacion = multiplicar
resultado = operacion(4, 5)
print(f"4 * 5 = {resultado}")

# Pasar función como argumento
def aplicar_operacion(func, a, b):
    """Aplica una función a dos números"""
    return func(a, b)

resultado = aplicar_operacion(sumar, 10, 20)
print(f"Suma aplicada: {resultado}")

resultado = aplicar_operacion(multiplicar, 6, 7)
print(f"Multiplicación aplicada: {resultado}")

# ========== FUNCIONES LAMBDA (ANÓNIMAS) ==========

# Lambda básica
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")

# Lambda con múltiples parámetros
sumar_lambda = lambda a, b: a + b
print(f"Suma lambda: {sumar_lambda(3, 4)}")

# Lambda con condicional
mayor = lambda x, y: x if x > y else y
print(f"Mayor entre 10 y 15: {mayor(10, 15)}")

# Lambda en funciones de orden superior
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Cuadrados: {cuadrados}")

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# ========== ALCANCE DE VARIABLES (SCOPE) ==========

# Variable global
variable_global = "Soy global"

def funcion_scope():
    """Demuestra el alcance de variables"""
    # Variable local
    variable_local = "Soy local"
    print(f"Dentro de la función - Global: {variable_global}")
    print(f"Dentro de la función - Local: {variable_local}")

funcion_scope()
print(f"Fuera de la función - Global: {variable_global}")
# print(variable_local)  # Error: variable_local no está definida

# Modificar variable global
contador = 0

def incrementar():
    """Incrementa el contador global"""
    global contador
    contador += 1

incrementar()
incrementar()
print(f"Contador: {contador}")

# ========== FUNCIONES ANIDADAS ==========

def funcion_externa(x):
    """Función que contiene otra función"""
    def funcion_interna(y):
        return y * 2
    
    resultado = funcion_interna(x)
    return resultado

print(f"Resultado función anidada: {funcion_externa(5)}")

# Closure: función interna que recuerda variables externas
def crear_multiplicador(factor):
    """Crea una función multiplicadora"""
    def multiplicar(numero):
        return numero * factor
    return multiplicar

multiplicar_por_2 = crear_multiplicador(2)
multiplicar_por_3 = crear_multiplicador(3)

print(f"5 * 2 = {multiplicar_por_2(5)}")
print(f"5 * 3 = {multiplicar_por_3(5)}")

# ========== DOCSTRINGS Y ANOTACIONES DE TIPO ==========

def calcular_area_rectangulo(ancho: float, alto: float) -> float:
    """
    Calcula el área de un rectángulo.
    
    Args:
        ancho: Ancho del rectángulo
        alto: Alto del rectángulo
    
    Returns:
        El área del rectángulo
    """
    return ancho * alto

area = calcular_area_rectangulo(5.0, 3.0)
print(f"Área del rectángulo: {area}")

# ========== EJEMPLOS PRÁCTICOS ==========

# Función recursiva: Factorial
def factorial(n):
    """Calcula el factorial de n recursivamente"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial de 5: {factorial(5)}")

# Función recursiva: Fibonacci
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(7): {fibonacci(7)}")

# Función con validación
def dividir(a, b):
    """Divide dos números con validación"""
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

print(f"10 / 2 = {dividir(10, 2)}")
print(f"10 / 0 = {dividir(10, 0)}")

# Función que retorna múltiples valores
def obtener_nombre_completo(nombre, apellido):
    """Retorna nombre completo y su longitud"""
    nombre_completo = f"{nombre} {apellido}"
    longitud = len(nombre_completo)
    return nombre_completo, longitud

nombre, longitud = obtener_nombre_completo("Juan", "Pérez")
print(f"Nombre: {nombre}, Longitud: {longitud}")
