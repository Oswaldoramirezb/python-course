"""
FUNCIÓN: CLOSURE
================
Función interna que recuerda variables externas
"""

print("=" * 50)
print("CLOSURES")
print("=" * 50)

# Closure básico
def crear_contador():
    """Crea un contador que recuerda su estado"""
    contador = 0
    
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    
    return incrementar

contador1 = crear_contador()
contador2 = crear_contador()

print("\nClosure - Contador:")
print(f"  contador1() = {contador1()}")
print(f"  contador1() = {contador1()}")
print(f"  contador2() = {contador2()} (independiente)")

# Closure con parámetros
def crear_multiplicador(factor):
    """Crea una función multiplicadora"""
    def multiplicar(numero):
        return numero * factor
    return multiplicar

multiplicar_por_5 = crear_multiplicador(5)
print(f"\nClosure - Multiplicador:")
print(f"  multiplicar_por_5(10) = {multiplicar_por_5(10)}")

print("\n" + "=" * 50)
