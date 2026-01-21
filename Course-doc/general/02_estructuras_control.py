"""
ESTRUCTURAS DE CONTROL - Condicionales y Bucles
===============================================
"""

# ========== CONDICIONALES: IF, ELIF, ELSE ==========

# Estructura básica if
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

# If-else
temperatura = 25
if temperatura > 30:
    print("Hace mucho calor")
else:
    print("La temperatura está bien")

# If-elif-else
nota = 85
if nota >= 90:
    print("Excelente (A)")
elif nota >= 80:
    print("Muy bien (B)")
elif nota >= 70:
    print("Bien (C)")
elif nota >= 60:
    print("Suficiente (D)")
else:
    print("Insuficiente (F)")

# Condicionales anidados
usuario_activo = True
saldo = 1000
if usuario_activo:
    if saldo > 0:
        print("Puedes realizar transacciones")
    else:
        print("Tu cuenta está sin saldo")
else:
    print("Usuario inactivo")

# Operador ternario
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

# ========== BUCLES: FOR ==========

# Bucle for con range
print("\n--- Bucle for con range ---")
for i in range(5):
    print(f"Índice: {i}")

# Range con inicio y fin
for i in range(2, 6):
    print(f"Número: {i}")

# Range con paso
for i in range(0, 10, 2):
    print(f"Pares: {i}")

# Bucle for con lista
frutas = ["manzana", "banana", "naranja"]
print("\n--- Bucle for con lista ---")
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Bucle for con enumerate (índice y valor)
print("\n--- Bucle for con enumerate ---")
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Bucle for con diccionario
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("\n--- Bucle for con diccionario ---")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Bucle for con zip (iterar múltiples listas)
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
print("\n--- Bucle for con zip ---")
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# ========== BUCLES: WHILE ==========

# Bucle while básico
print("\n--- Bucle while básico ---")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Bucle while con condición
numero = 10
print("\n--- Bucle while con condición ---")
while numero > 0:
    print(f"Número: {numero}")
    numero -= 2

# Bucle while con break
print("\n--- Bucle while con break ---")
contador = 0
while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador >= 5:
        break

# ========== CONTROL DE FLUJO: BREAK, CONTINUE, PASS ==========

# Break: salir del bucle
print("\n--- Uso de break ---")
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue: saltar a la siguiente iteración
print("\n--- Uso de continue ---")
for i in range(10):
    if i % 2 == 0:
        continue  # Salta los números pares
    print(i)

# Pass: placeholder (no hace nada)
print("\n--- Uso de pass ---")
for i in range(5):
    if i == 2:
        pass  # No hace nada, solo mantiene la sintaxis
    print(i)

# ========== BUCLES ANIDADOS ==========

# Tabla de multiplicar
print("\n--- Bucles anidados: Tabla de multiplicar ---")
for i in range(1, 4):
    for j in range(1, 4):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

# Matriz
print("\n--- Bucles anidados: Matriz ---")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Nueva línea

# ========== EJEMPLOS PRÁCTICOS ==========

# Buscar un elemento en una lista
print("\n--- Ejemplo: Buscar elemento ---")
numeros = [1, 3, 5, 7, 9, 11]
buscar = 7
encontrado = False

for num in numeros:
    if num == buscar:
        encontrado = True
        print(f"¡Encontrado! {buscar} está en la lista")
        break

if not encontrado:
    print(f"{buscar} no está en la lista")

# Sumar números hasta que el usuario ingrese 0
print("\n--- Ejemplo: Suma acumulativa ---")
suma = 0
# Simulamos entrada del usuario
entradas = [5, 10, 15, 0]
indice = 0

while True:
    # numero = int(input("Ingresa un número (0 para salir): "))
    numero = entradas[indice]
    indice += 1
    if numero == 0:
        break
    suma += numero
    print(f"Suma acumulada: {suma}")

# Contar vocales en una cadena
print("\n--- Ejemplo: Contar vocales ---")
texto = "Programación en Python"
vocales = "aeiouAEIOU"
contador_vocales = 0

for letra in texto:
    if letra in vocales:
        contador_vocales += 1

print(f"El texto '{texto}' tiene {contador_vocales} vocales")

# Validar contraseña
print("\n--- Ejemplo: Validar contraseña ---")
contraseña = "Python123"
tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False

for caracter in contraseña:
    if caracter.isupper():
        tiene_mayuscula = True
    elif caracter.islower():
        tiene_minuscula = True
    elif caracter.isdigit():
        tiene_numero = True

if len(contraseña) >= 8 and tiene_mayuscula and tiene_minuscula and tiene_numero:
    print("Contraseña válida")
else:
    print("Contraseña inválida")
