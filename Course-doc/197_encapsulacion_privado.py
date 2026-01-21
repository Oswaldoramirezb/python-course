"""
ENCAPSULACIÓN: PRIVADO
=======================
Atributos privados (convención: __atributo)
"""

print("=" * 50)
print("ENCAPSULACIÓN PRIVADA")
print("=" * 50)

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        # Atributo privado (dos guiones bajos)
        self.__saldo = saldo_inicial
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito de ${cantidad} realizado"
        return "Cantidad inválida"
    
    def obtener_saldo(self):
        """Getter para saldo privado"""
        return self.__saldo

cuenta = CuentaBancaria("Juan", 1000)
print("\nAtributo privado:")
print(f"  self.__saldo = {cuenta.obtener_saldo()}")

print("\nAcceso:")
print("  ❌ cuenta.__saldo → AttributeError")
print("  ✅ cuenta.obtener_saldo() = {cuenta.obtener_saldo()}")

print("\nModificar solo a través de métodos:")
print(f"  cuenta.depositar(500) = {cuenta.depositar(500)}")
print(f"  cuenta.obtener_saldo() = {cuenta.obtener_saldo()}")

print("\nName mangling:")
print("  Python renombra __saldo a _CuentaBancaria__saldo")
print("  Esto previene accesos accidentales")

print("\n" + "=" * 50)
