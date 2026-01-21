"""
ESTRUCTURAS DE DATOS - Listas, Tuplas, Diccionarios y Sets
===========================================================
"""

# ========== LISTAS ==========

# Crear listas
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "naranja"]
mixta = [1, "dos", 3.0, True]

# Acceder a elementos
print(f"Primer elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")
print(f"Subconjunto: {numeros[1:4]}")

# Modificar elementos
numeros[0] = 10
print(f"Lista modificada: {numeros}")

# Agregar elementos
numeros.append(6)  # Agrega al final
numeros.insert(0, 0)  # Inserta en posición específica
print(f"Después de agregar: {numeros}")

# Eliminar elementos
numeros.remove(10)  # Elimina el valor 10
eliminado = numeros.pop()  # Elimina y retorna el último
del numeros[0]  # Elimina por índice
print(f"Después de eliminar: {numeros}")

# Métodos útiles de listas
lista = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Longitud: {len(lista)}")
print(f"Máximo: {max(lista)}")
print(f"Mínimo: {min(lista)}")
print(f"Suma: {sum(lista)}")
print(f"Conteo de 1: {lista.count(1)}")
print(f"Índice de 4: {lista.index(4)}")

# Ordenar listas
lista.sort()  # Ordena in-place
print(f"Ordenada: {lista}")
lista.sort(reverse=True)  # Orden descendente
print(f"Orden descendente: {lista}")

lista2 = [3, 1, 4, 1, 5]
lista_ordenada = sorted(lista2)  # Retorna nueva lista ordenada
print(f"Original: {lista2}, Ordenada: {lista_ordenada}")

# Listas anidadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matriz[1][2]: {matriz[1][2]}")

# Comprensión de listas (List Comprehension)
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares: {pares}")

# ========== TUPLAS ==========

# Crear tuplas
coordenadas = (3, 4)
colores = ("rojo", "verde", "azul")
tupla_vacia = ()
tupla_un_elemento = (5,)  # Nota la coma

# Las tuplas son inmutables
print(f"Coordenadas: {coordenadas}")
# coordenadas[0] = 5  # Error: las tuplas son inmutables

# Desempaquetado de tuplas
x, y = coordenadas
print(f"x: {x}, y: {y}")

# Tuplas como retorno de funciones
def obtener_nombre_edad():
    return "Juan", 30

nombre, edad = obtener_nombre_edad()
print(f"Nombre: {nombre}, Edad: {edad}")

# Métodos de tuplas
tupla = (1, 2, 3, 2, 4, 2)
print(f"Conteo de 2: {tupla.count(2)}")
print(f"Índice de 3: {tupla.index(3)}")

# ========== DICCIONARIOS ==========

# Crear diccionarios
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a valores
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")
print(f"Email: {persona.get('email', 'No disponible')}")  # Valor por defecto

# Modificar y agregar
persona["edad"] = 31
persona["email"] = "juan@email.com"
print(f"Persona actualizada: {persona}")

# Eliminar elementos
del persona["email"]
email = persona.pop("ciudad", None)  # Retorna None si no existe
print(f"Después de eliminar: {persona}")

# Métodos útiles
print(f"Claves: {persona.keys()}")
print(f"Valores: {persona.values()}")
print(f"Items: {persona.items()}")

# Iterar sobre diccionarios
for clave in persona:
    print(f"{clave}: {persona[clave]}")

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Diccionarios anidados
estudiantes = {
    "estudiante1": {"nombre": "Ana", "nota": 85},
    "estudiante2": {"nombre": "Luis", "nota": 92}
}
print(f"Nota de estudiante1: {estudiantes['estudiante1']['nota']}")

# Comprensión de diccionarios
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados dict: {cuadrados_dict}")

# ========== SETS (CONJUNTOS) ==========

# Crear sets
numeros_set = {1, 2, 3, 4, 5}
colores_set = set(["rojo", "verde", "azul"])
set_vacio = set()  # No usar {} para set vacío

# Los sets no permiten duplicados
duplicados = {1, 2, 2, 3, 3, 3}
print(f"Set sin duplicados: {duplicados}")

# Agregar y eliminar elementos
numeros_set.add(6)
numeros_set.remove(1)  # Error si no existe
numeros_set.discard(10)  # No da error si no existe
print(f"Set modificado: {numeros_set}")

# Operaciones con sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2  # o set1.union(set2)
print(f"Unión: {union}")

interseccion = set1 & set2  # o set1.intersection(set2)
print(f"Intersección: {interseccion}")

diferencia = set1 - set2  # o set1.difference(set2)
print(f"Diferencia: {diferencia}")

diferencia_simetrica = set1 ^ set2  # o set1.symmetric_difference(set2)
print(f"Diferencia simétrica: {diferencia_simetrica}")

# Verificar pertenencia
print(f"¿3 está en set1? {3 in set1}")
print(f"¿9 está en set1? {9 in set1}")

# ========== OPERACIONES COMUNES ==========

# Copiar listas
lista_original = [1, 2, 3]
lista_copia = lista_original.copy()  # Copia superficial
lista_copia2 = lista_original[:]  # Otra forma de copiar

# Copiar diccionarios
dict_original = {"a": 1, "b": 2}
dict_copia = dict_original.copy()

# Verificar si está vacío
lista_vacia = []
if not lista_vacia:
    print("La lista está vacía")

# Combinar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_combinada = lista1 + lista2
print(f"Listas combinadas: {lista_combinada}")

# Extender lista
lista1.extend([7, 8, 9])
print(f"Lista extendida: {lista1}")

# ========== EJEMPLOS PRÁCTICOS ==========

# Contar elementos únicos
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unicos = len(set(lista_con_duplicados))
print(f"Elementos únicos: {unicos}")

# Invertir un diccionario
diccionario = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in diccionario.items()}
print(f"Diccionario invertido: {invertido}")

# Filtrar elementos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(f"Números pares: {pares}")

# Agrupar datos
estudiantes = [
    {"nombre": "Ana", "curso": "Python"},
    {"nombre": "Luis", "curso": "Java"},
    {"nombre": "María", "curso": "Python"},
    {"nombre": "Pedro", "curso": "Java"}
]

# Agrupar por curso (usando diccionario)
cursos = {}
for estudiante in estudiantes:
    curso = estudiante["curso"]
    if curso not in cursos:
        cursos[curso] = []
    cursos[curso].append(estudiante["nombre"])

print(f"Estudiantes por curso: {cursos}")

# Encontrar elementos comunes
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comunes = set(lista1) & set(lista2)
print(f"Elementos comunes: {comunes}")
