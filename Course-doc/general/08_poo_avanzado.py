"""
PROGRAMACIÓN ORIENTADA A OBJETOS (POO) - Avanzado
=================================================
Herencia, Polimorfismo, Encapsulación y Abstracción
"""

# ========== HERENCIA BÁSICA ==========

class Animal:
    """Clase base (padre)"""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        """Método que será sobrescrito en las clases hijas"""
        return "El animal hace un sonido"
    
    def presentarse(self):
        """Método compartido por todas las clases hijas"""
        return f"Soy {self.nombre} y tengo {self.edad} años"

class Perro(Animal):
    """Clase hija que hereda de Animal"""
    
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamar al constructor del padre
        self.raza = raza
    
    def hacer_sonido(self):
        """Sobrescribe el método del padre"""
        return "¡Guau guau!"
    
    def ladrar(self):
        """Método específico de Perro"""
        return f"{self.nombre} está ladrando"

class Gato(Animal):
    """Otra clase hija"""
    
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def hacer_sonido(self):
        """Sobrescribe el método del padre"""
        return "¡Miau miau!"
    
    def ronronear(self):
        """Método específico de Gato"""
        return f"{self.nombre} está ronroneando"

# Crear instancias
perro = Perro("Max", 3, "Labrador")
gato = Gato("Luna", 2, "Negro")

print("=== HERENCIA BÁSICA ===")
print(perro.presentarse())
print(perro.hacer_sonido())
print(perro.ladrar())

print(gato.presentarse())
print(gato.hacer_sonido())
print(gato.ronronear())

# ========== POLIMORFISMO ==========

def hacer_ruido_animal(animal):
    """Función que demuestra polimorfismo"""
    print(f"{animal.nombre}: {animal.hacer_sonido()}")

print("\n=== POLIMORFISMO ===")
animales = [perro, gato]
for animal in animales:
    hacer_ruido_animal(animal)

# ========== HERENCIA MÚLTIPLE ==========

class Volador:
    """Clase mixin para objetos que vuelan"""
    
    def volar(self):
        return "Estoy volando"
    
    def aterrizar(self):
        return "Aterrizando"

class Nadador:
    """Clase mixin para objetos que nadan"""
    
    def nadar(self):
        return "Estoy nadando"
    
    def sumergirse(self):
        return "Sumergiéndome"

class Pato(Animal, Volador, Nadador):
    """Clase que hereda de múltiples clases"""
    
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def hacer_sonido(self):
        return "¡Cuac cuac!"

pato = Pato("Donald", 5)
print("\n=== HERENCIA MÚLTIPLE ===")
print(pato.presentarse())
print(pato.hacer_sonido())
print(pato.volar())
print(pato.nadar())

# ========== MÉTODO RESOLUTION ORDER (MRO) ==========

print("\n=== MRO (Method Resolution Order) ===")
print(f"MRO de Pato: {Pato.__mro__}")

# ========== ENCAPSULACIÓN AVANZADA ==========

class CuentaSegura:
    """Ejemplo de encapsulación con propiedades"""
    
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self.__saldo = saldo_inicial  # Privado
        self.__historial = []  # Privado
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, valor):
        if isinstance(valor, str) and len(valor) > 0:
            self._titular = valor
        else:
            raise ValueError("El titular debe ser una cadena no vacía")
    
    @property
    def saldo(self):
        """Solo lectura para saldo"""
        return self.__saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            self.__historial.append(f"Depósito: +${cantidad}")
            return True
        return False
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            self.__historial.append(f"Retiro: -${cantidad}")
            return True
        return False
    
    def obtener_historial(self):
        """Obtiene una copia del historial"""
        return self.__historial.copy()

cuenta = CuentaSegura("Juan", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(f"\n=== ENCAPSULACIÓN ===")
print(f"Saldo: ${cuenta.saldo}")
print(f"Historial: {cuenta.obtener_historial()}")

# ========== CLASES ABSTRACTAS ==========

from abc import ABC, abstractmethod

class Forma(ABC):
    """Clase abstracta base"""
    
    @abstractmethod
    def calcular_area(self):
        """Método abstracto que debe ser implementado"""
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        """Método abstracto que debe ser implementado"""
        pass
    
    def describir(self):
        """Método concreto (no abstracto)"""
        return f"Área: {self.calcular_area()}, Perímetro: {self.calcular_perimetro()}"

class Circulo(Forma):
    """Implementación concreta de Forma"""
    
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        import math
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        import math
        return 2 * math.pi * self.radio

class Rectangulo(Forma):
    """Otra implementación concreta"""
    
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

print("\n=== CLASES ABSTRACTAS ===")
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

print(f"Círculo: {circulo.describir()}")
print(f"Rectángulo: {rectangulo.describir()}")

# ========== MÉTODOS ESPECIALES AVANZADOS ==========

class Vector:
    """Clase que representa un vector matemático"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        """Sobrecarga del operador +"""
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __sub__(self, otro):
        """Sobrecarga del operador -"""
        return Vector(self.x - otro.x, self.y - otro.y)
    
    def __mul__(self, escalar):
        """Sobrecarga del operador *"""
        return Vector(self.x * escalar, self.y * escalar)
    
    def __eq__(self, otro):
        """Sobrecarga del operador =="""
        return self.x == otro.x and self.y == otro.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        """Retorna la magnitud del vector"""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("\n=== SOBRECARGA DE OPERADORES ===")
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"Magnitud de v1: {len(v1)}")

# ========== COMPOSICIÓN vs HERENCIA ==========

class Motor:
    """Clase que representa un motor"""
    
    def __init__(self, potencia):
        self.potencia = potencia
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        return "Motor encendido"
    
    def apagar(self):
        self.encendido = False
        return "Motor apagado"

class Coche:
    """Clase que usa composición (tiene un motor)"""
    
    def __init__(self, marca, modelo, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # Composición
    
    def arrancar(self):
        return f"{self.marca} {self.modelo}: {self.motor.encender()}"
    
    def detener(self):
        return f"{self.marca} {self.modelo}: {self.motor.apagar()}"

coche = Coche("Toyota", "Corolla", 150)
print("\n=== COMPOSICIÓN ===")
print(coche.arrancar())
print(coche.detener())

# ========== EJEMPLO COMPLETO: SISTEMA DE EMPLEADOS ==========

class Empleado(ABC):
    """Clase abstracta base para empleados"""
    
    def __init__(self, nombre, empleado_id):
        self.nombre = nombre
        self.empleado_id = empleado_id
    
    @abstractmethod
    def calcular_salario(self):
        pass
    
    def __str__(self):
        return f"{self.nombre} (ID: {self.empleado_id})"

class EmpleadoTiempoCompleto(Empleado):
    """Empleado con salario fijo"""
    
    def __init__(self, nombre, empleado_id, salario_mensual):
        super().__init__(nombre, empleado_id)
        self.salario_mensual = salario_mensual
    
    def calcular_salario(self):
        return self.salario_mensual

class EmpleadoPorHora(Empleado):
    """Empleado que cobra por horas"""
    
    def __init__(self, nombre, empleado_id, horas_trabajadas, tarifa_hora):
        super().__init__(nombre, empleado_id)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
    
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_hora

class Gerente(EmpleadoTiempoCompleto):
    """Gerente que hereda de EmpleadoTiempoCompleto"""
    
    def __init__(self, nombre, empleado_id, salario_mensual, bono):
        super().__init__(nombre, empleado_id, salario_mensual)
        self.bono = bono
    
    def calcular_salario(self):
        return self.salario_mensual + self.bono

print("\n=== SISTEMA DE EMPLEADOS ===")
empleados = [
    EmpleadoTiempoCompleto("Ana", "E001", 3000),
    EmpleadoPorHora("Luis", "E002", 160, 20),
    Gerente("María", "E003", 5000, 1000)
]

for empleado in empleados:
    print(f"{empleado}: ${empleado.calcular_salario()}")
