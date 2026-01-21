"""
DECORADOR: DE CLASE
===================
Aplicar decoradores a clases
"""

print("=" * 50)
print("DECORADOR DE CLASE")
print("=" * 50)

# Decorador de clase
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

print("\nDecorador de clase:")
print("  @decorador_clase")
print("  class MiClase:")
print("      ...")

obj = MiClase(42)
print(f"\nUsar objeto:")
print(f"  obj.mostrar() = {obj.mostrar()}")

# Decorador como clase
class ContadorLlamadas:
    """Decorador de clase que cuenta llamadas"""
    def __init__(self, func):
        self.func = func
        self.contador = 0
    
    def __call__(self, *args, **kwargs):
        self.contador += 1
        print(f"  {self.func.__name__} ha sido llamada {self.contador} veces")
        return self.func(*args, **kwargs)

@ContadorLlamadas
def saludar():
    return "Hola"

print("\nDecorador como clase:")
print("  @ContadorLlamadas")
print("  def saludar(): ...")

saludar()
saludar()
saludar()

print("\n" + "=" * 50)
