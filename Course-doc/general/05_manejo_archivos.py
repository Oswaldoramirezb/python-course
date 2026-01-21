"""
MANEJO DE ARCHIVOS - Leer y Escribir Archivos
==============================================
"""

import os
import json
import csv

# ========== LECTURA DE ARCHIVOS ==========

# Leer archivo completo
def leer_archivo_completo(nombre_archivo):
    """Lee todo el contenido de un archivo"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return f"Error: El archivo {nombre_archivo} no existe"

# Leer archivo línea por línea
def leer_archivo_lineas(nombre_archivo):
    """Lee un archivo línea por línea"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        return lineas
    except FileNotFoundError:
        return []

# Leer archivo iterando sobre líneas
def leer_archivo_iterativo(nombre_archivo):
    """Lee un archivo iterando sobre cada línea"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                print(f"Línea {numero_linea}: {linea.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe")

# ========== ESCRITURA DE ARCHIVOS ==========

# Escribir archivo (sobrescribe)
def escribir_archivo(nombre_archivo, contenido):
    """Escribe contenido en un archivo (sobrescribe si existe)"""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
    print(f"Archivo {nombre_archivo} escrito correctamente")

# Agregar al final de un archivo
def agregar_al_archivo(nombre_archivo, contenido):
    """Agrega contenido al final de un archivo"""
    with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
        archivo.write(contenido)
    print(f"Contenido agregado a {nombre_archivo}")

# Escribir múltiples líneas
def escribir_lineas(nombre_archivo, lineas):
    """Escribe múltiples líneas en un archivo"""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.writelines(lineas)
    print(f"Líneas escritas en {nombre_archivo}")

# ========== EJEMPLOS PRÁCTICOS ==========

# Crear y escribir un archivo de ejemplo
contenido_ejemplo = """Este es un archivo de ejemplo.
Contiene múltiples líneas.
Python es genial para manejar archivos."""

escribir_archivo("ejemplo.txt", contenido_ejemplo)

# Leer el archivo creado
print("\n--- Contenido del archivo ---")
contenido = leer_archivo_completo("ejemplo.txt")
print(contenido)

# Agregar más contenido
agregar_al_archivo("ejemplo.txt", "\nEsta línea fue agregada después.")

# ========== MANEJO DE ARCHIVOS JSON ==========

# Escribir JSON
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["leer", "programar", "viajar"]
}

def escribir_json(nombre_archivo, datos):
    """Escribe datos en formato JSON"""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print(f"Datos JSON escritos en {nombre_archivo}")

escribir_json("datos.json", datos)

# Leer JSON
def leer_json(nombre_archivo):
    """Lee datos desde un archivo JSON"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        return None

datos_leidos = leer_json("datos.json")
print(f"\n--- Datos JSON leídos ---")
print(datos_leidos)

# ========== MANEJO DE ARCHIVOS CSV ==========

# Escribir CSV
def escribir_csv(nombre_archivo, datos, encabezados):
    """Escribe datos en formato CSV"""
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezados)
        escritor.writerows(datos)
    print(f"Datos CSV escritos en {nombre_archivo}")

encabezados = ["Nombre", "Edad", "Ciudad"]
datos_csv = [
    ["Ana", 25, "Barcelona"],
    ["Luis", 30, "Madrid"],
    ["María", 28, "Valencia"]
]

escribir_csv("personas.csv", datos_csv, encabezados)

# Leer CSV
def leer_csv(nombre_archivo):
    """Lee datos desde un archivo CSV"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            datos = []
            for fila in lector:
                datos.append(fila)
            return encabezados, datos
    except FileNotFoundError:
        return None, None

encabezados, datos = leer_csv("personas.csv")
print(f"\n--- Datos CSV leídos ---")
print(f"Encabezados: {encabezados}")
for fila in datos:
    print(fila)

# Leer CSV como diccionario
def leer_csv_dict(nombre_archivo):
    """Lee CSV y retorna lista de diccionarios"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)
    except FileNotFoundError:
        return []

personas_dict = leer_csv_dict("personas.csv")
print(f"\n--- CSV como diccionarios ---")
for persona in personas_dict:
    print(persona)

# ========== OPERACIONES CON ARCHIVOS ==========

# Verificar si un archivo existe
def archivo_existe(nombre_archivo):
    """Verifica si un archivo existe"""
    return os.path.exists(nombre_archivo)

print(f"\n¿Existe ejemplo.txt? {archivo_existe('ejemplo.txt')}")

# Obtener información del archivo
def info_archivo(nombre_archivo):
    """Obtiene información de un archivo"""
    if os.path.exists(nombre_archivo):
        tamaño = os.path.getsize(nombre_archivo)
        return f"Tamaño: {tamaño} bytes"
    return "Archivo no existe"

print(info_archivo("ejemplo.txt"))

# Listar archivos en un directorio
def listar_archivos(directorio="."):
    """Lista archivos en un directorio"""
    archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
    return archivos

print(f"\n--- Archivos en el directorio actual ---")
for archivo in listar_archivos():
    print(archivo)

# ========== CONTEXT MANAGER PERSONALIZADO ==========

class ArchivoSeguro:
    """Context manager para manejo seguro de archivos"""
    
    def __init__(self, nombre_archivo, modo='r'):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
    
    def __enter__(self):
        self.archivo = open(self.nombre_archivo, self.modo, encoding='utf-8')
        return self.archivo
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
        if self.archivo:
            self.archivo.close()
        return False  # No suprime excepciones

# Uso del context manager personalizado
with ArchivoSeguro("ejemplo.txt", 'r') as archivo:
    contenido = archivo.read()
    print(f"\n--- Leído con context manager personalizado ---")
    print(contenido[:50] + "...")

# ========== EJEMPLO COMPLETO: LOGGER SIMPLE ==========

class Logger:
    """Sistema de logging simple a archivo"""
    
    def __init__(self, nombre_archivo="log.txt"):
        self.nombre_archivo = nombre_archivo
    
    def log(self, mensaje, nivel="INFO"):
        """Registra un mensaje en el archivo de log"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"[{timestamp}] [{nivel}] {mensaje}\n"
        with open(self.nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(linea)
    
    def info(self, mensaje):
        self.log(mensaje, "INFO")
    
    def error(self, mensaje):
        self.log(mensaje, "ERROR")
    
    def warning(self, mensaje):
        self.log(mensaje, "WARNING")

# Uso del logger
logger = Logger("aplicacion.log")
logger.info("Aplicación iniciada")
logger.warning("Advertencia: memoria baja")
logger.error("Error al conectar a la base de datos")

print("\n--- Contenido del log ---")
print(leer_archivo_completo("aplicacion.log"))
