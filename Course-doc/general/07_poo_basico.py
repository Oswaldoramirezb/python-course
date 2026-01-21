"""
PROGRAMACIÓN ORIENTADA A OBJETOS (POO) - Básico
===============================================
Clases, Objetos, Métodos y Atributos
"""

# ========== CLASE BÁSICA ==========

class Persona:
    """Clase que representa una persona"""
    
    # Atributo de clase (compartido por todas las instancias)
    especie = "Homo sapiens"
    
    def __init__(self, nombre, edad):
        """Constructor: inicializa los atributos de instancia"""
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia
    
    def presentarse(self):
        """Método de instancia"""
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
    def cumplir_anios(self):
        """Método que modifica el estado del objeto"""
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tengo {self.edad} años"

# Crear objetos (instancias)
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

print(persona1.presentarse())
print(persona2.presentarse())
print(f"Especie: {Persona.especie}")

# ========== MÉTODOS ESPECIALES (DUNDER METHODS) ==========

class Libro:
    """Clase que representa un libro"""
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        """Representación legible para humanos"""
        return f"'{self.titulo}' por {self.autor}"
    
    def __repr__(self):
        """Representación técnica para desarrolladores"""
        return f"Libro('{self.titulo}', '{self.autor}', {self.paginas})"
    
    def __len__(self):
        """Retorna la longitud (número de páginas)"""
        return self.paginas
    
    def __eq__(self, otro):
        """Compara si dos libros son iguales"""
        if isinstance(otro, Libro):
            return self.titulo == otro.titulo and self.autor == otro.autor
        return False

libro1 = Libro("Python Básico", "Autor X", 300)
libro2 = Libro("Python Básico", "Autor X", 250)

print(f"\nLibro: {libro1}")
print(f"Representación: {repr(libro1)}")
print(f"Páginas: {len(libro1)}")
print(f"¿Son iguales? {libro1 == libro2}")

# ========== ATRIBUTOS PRIVADOS (ENCAPSULACIÓN) ==========

class CuentaBancaria:
    """Clase que representa una cuenta bancaria"""
    
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (convención: __)
    
    def depositar(self, cantidad):
        """Deposita dinero en la cuenta"""
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito de ${cantidad} realizado. Saldo: ${self.__saldo}"
        return "La cantidad debe ser positiva"
    
    def retirar(self, cantidad):
        """Retira dinero de la cuenta"""
        if cantidad > 0:
            if cantidad <= self.__saldo:
                self.__saldo -= cantidad
                return f"Retiro de ${cantidad} realizado. Saldo: ${self.__saldo}"
            return "Fondos insuficientes"
        return "La cantidad debe ser positiva"
    
    def obtener_saldo(self):
        """Getter: obtiene el saldo"""
        return self.__saldo
    
    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.__saldo}"

cuenta = CuentaBancaria("Juan", 1000)
print(f"\n{cuenta}")
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(f"Saldo actual: ${cuenta.obtener_saldo()}")

# ========== PROPIEDADES (PROPERTIES) ==========

class Rectangulo:
    """Clase que representa un rectángulo"""
    
    def __init__(self, ancho, alto):
        self._ancho = ancho  # Atributo protegido
        self._alto = alto
    
    @property
    def ancho(self):
        """Getter para ancho"""
        return self._ancho
    
    @ancho.setter
    def ancho(self, valor):
        """Setter para ancho con validación"""
        if valor > 0:
            self._ancho = valor
        else:
            raise ValueError("El ancho debe ser positivo")
    
    @property
    def alto(self):
        """Getter para alto"""
        return self._alto
    
    @alto.setter
    def alto(self, valor):
        """Setter para alto con validación"""
        if valor > 0:
            self._alto = valor
        else:
            raise ValueError("El alto debe ser positivo")
    
    @property
    def area(self):
        """Propiedad calculada: área del rectángulo"""
        return self._ancho * self._alto
    
    @property
    def perimetro(self):
        """Propiedad calculada: perímetro del rectángulo"""
        return 2 * (self._ancho + self._alto)

rectangulo = Rectangulo(5, 3)
print(f"\nRectángulo: {rectangulo.ancho}x{rectangulo.alto}")
print(f"Área: {rectangulo.area}")
print(f"Perímetro: {rectangulo.perimetro}")

rectangulo.ancho = 10
print(f"Nuevo ancho: {rectangulo.ancho}")

# ========== MÉTODOS DE CLASE Y ESTÁTICOS ==========

class Utilidades:
    """Clase con métodos de clase y estáticos"""
    
    contador = 0  # Variable de clase
    
    def __init__(self):
        Utilidades.contador += 1
        self.id = Utilidades.contador
    
    @classmethod
    def obtener_contador(cls):
        """Método de clase: trabaja con la clase, no con instancias"""
        return cls.contador
    
    @classmethod
    def crear_desde_string(cls, cadena):
        """Método de clase alternativo para crear instancias"""
        # Ejemplo: crear desde "nombre:edad"
        partes = cadena.split(":")
        return cls(partes[0], int(partes[1]))
    
    @staticmethod
    def sumar(a, b):
        """Método estático: no necesita acceso a la clase ni instancia"""
        return a + b
    
    @staticmethod
    def es_par(numero):
        """Método estático: verifica si un número es par"""
        return numero % 2 == 0

util1 = Utilidades()
util2 = Utilidades()
print(f"\nContador de instancias: {Utilidades.obtener_contador()}")
print(f"Suma estática: {Utilidades.sumar(5, 3)}")
print(f"¿10 es par? {Utilidades.es_par(10)}")

# ========== EJEMPLO COMPLETO: SISTEMA DE ESTUDIANTES ==========

class Estudiante:
    """Clase que representa un estudiante"""
    
    total_estudiantes = 0
    
    def __init__(self, nombre, estudiante_id, curso="Python"):
        self.nombre = nombre
        self.estudiante_id = estudiante_id
        self.curso = curso
        self.notas = []
        Estudiante.total_estudiantes += 1
    
    def agregar_nota(self, nota):
        """Agrega una nota al estudiante"""
        if 0 <= nota <= 100:
            self.notas.append(nota)
            return f"Nota {nota} agregada"
        return "Nota inválida (debe estar entre 0 y 100)"
    
    def calcular_promedio(self):
        """Calcula el promedio de notas"""
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0
    
    def obtener_estado(self):
        """Obtiene el estado académico"""
        promedio = self.calcular_promedio()
        if promedio >= 90:
            return "Excelente"
        elif promedio >= 80:
            return "Muy bien"
        elif promedio >= 70:
            return "Bien"
        elif promedio >= 60:
            return "Suficiente"
        else:
            return "Insuficiente"
    
    @classmethod
    def obtener_total(cls):
        """Retorna el total de estudiantes"""
        return cls.total_estudiantes
    
    def __str__(self):
        promedio = self.calcular_promedio()
        return f"Estudiante: {self.nombre} (ID: {self.estudiante_id}) - Promedio: {promedio:.2f}"

# Crear estudiantes
estudiante1 = Estudiante("Ana", "E001")
estudiante1.agregar_nota(85)
estudiante1.agregar_nota(90)
estudiante1.agregar_nota(88)

estudiante2 = Estudiante("Luis", "E002", "Java")
estudiante2.agregar_nota(75)
estudiante2.agregar_nota(80)

print(f"\n{estudiante1}")
print(f"Estado: {estudiante1.obtener_estado()}")
print(f"\n{estudiante2}")
print(f"Estado: {estudiante2.obtener_estado()}")
print(f"\nTotal de estudiantes: {Estudiante.obtener_total()}")
