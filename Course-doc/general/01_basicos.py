"""
PYTHON BÁSICO - Variables, Tipos de Datos y Operadores
=======================================================
"""

# ========== VARIABLES Y TIPOS DE DATOS ==========

# Números enteros (int)
edad = 25
temperatura = -10
numero_grande = 1000000

# Números flotantes (float)
precio = 19.99
pi = 3.14159
nota = 8.5

# Cadenas de texto (str)
nombre = "Juan"
apellido = 'Pérez'
mensaje = """Este es un mensaje
que puede tener múltiples líneas"""

# Booleanos (bool)
es_estudiante = True
tiene_trabajo = False

# None (tipo NoneType)
valor_nulo = None

# ========== OPERADORES ARITMÉTICOS ==========
a = 10
b = 3

suma = a + b          # 13
resta = a - b         # 7
multiplicacion = a * b  # 30
division = a / b      # 3.333...
division_entera = a // b  # 3
modulo = a % b        # 1 (resto de la división)
potencia = a ** b     # 1000

# ========== OPERADORES DE COMPARACIÓN ==========
x = 5
y = 10

igual = x == y        # False
diferente = x != y    # True
mayor = x > y         # False
menor = x < y         # True
mayor_igual = x >= y  # False
menor_igual = x <= y  # True

# ========== OPERADORES LÓGICOS ==========
p = True
q = False

and_logico = p and q      # False
or_logico = p or q        # True
not_logico = not p        # False

# ========== OPERADORES DE ASIGNACIÓN ==========
numero = 10
numero += 5   # numero = numero + 5  -> 15
numero -= 3   # numero = numero - 3  -> 12
numero *= 2   # numero = numero * 2  -> 24
numero /= 4   # numero = numero / 4  -> 6.0
numero //= 2  # numero = numero // 2 -> 3.0
numero %= 2   # numero = numero % 2  -> 1.0
numero **= 3  # numero = numero ** 3 -> 1.0

# ========== CONVERSIÓN DE TIPOS ==========
# Convertir a entero
texto_numero = "123"
numero_entero = int(texto_numero)  # 123
decimal = int(45.7)  # 45 (trunca)

# Convertir a flotante
numero_str = "3.14"
numero_float = float(numero_str)  # 3.14
entero = float(5)  # 5.0

# Convertir a cadena
edad_str = str(25)  # "25"
precio_str = str(19.99)  # "19.99"

# Convertir a booleano
bool_1 = bool(1)      # True
bool_0 = bool(0)      # False
bool_vacio = bool("")  # False
bool_texto = bool("hola")  # True

# ========== OPERACIONES CON CADENAS ==========
nombre_completo = "Juan" + " " + "Pérez"  # Concatenación
saludo = "Hola " * 3  # "Hola Hola Hola "
longitud = len("Python")  # 6

# Formateo de cadenas (f-strings - Python 3.6+)
nombre = "María"
edad = 30
mensaje = f"Mi nombre es {nombre} y tengo {edad} años"

# Formateo con .format()
mensaje2 = "Mi nombre es {} y tengo {} años".format(nombre, edad)

# Formateo con % (estilo antiguo)
mensaje3 = "Mi nombre es %s y tengo %d años" % (nombre, edad)

# ========== ENTRADA Y SALIDA ==========
# Entrada (comentado para evitar errores al ejecutar)
# nombre_usuario = input("Ingresa tu nombre: ")
# edad_usuario = int(input("Ingresa tu edad: "))

# Salida
print("Hola, mundo!")
print("Nombre:", nombre, "Edad:", edad)
print(f"Bienvenido {nombre}")

# ========== EJEMPLOS PRÁCTICOS ==========

# Calcular área de un círculo
radio = 5.0
area = 3.14159 * radio ** 2
print(f"El área del círculo es: {area}")

# Operaciones con diferentes tipos
resultado = "El resultado es: " + str(10 + 5)
print(resultado)

# Verificar tipo de variable
tipo_variable = type(edad)
print(f"El tipo de 'edad' es: {tipo_variable}")

# Verificar si una variable es de un tipo específico
es_entero = isinstance(edad, int)  # True
es_cadena = isinstance(nombre, str)  # True
