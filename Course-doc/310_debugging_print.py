"""
DEBUGGING: PRINT
================
Usar print() para debugging
"""

print("=" * 50)
print("DEBUGGING CON PRINT()")
print("=" * 50)

print("\nPrint básico:")
print("  print(variable) - Ver valor")
print("  print(f'Variable: {variable}') - Con formato")

# Ejemplo
def sumar(a, b):
    print(f"  DEBUG: sumar({a}, {b})")
    resultado = a + b
    print(f"  DEBUG: resultado = {resultado}")
    return resultado

print("\nEjemplo:")
resultado = sumar(5, 3)
print(f"  Resultado final: {resultado}")

print("\nTécnicas:")
print("  - Agregar prints en puntos clave")
print("  - Mostrar valores de variables")
print("  - Verificar flujo de ejecución")
print("  - Identificar dónde falla")

# Debugging de lista
print("\nDebugging de lista:")
lista = [1, 2, 3, 4, 5]
print(f"  lista = {lista}")
print(f"  len(lista) = {len(lista)}")

for i, elemento in enumerate(lista):
    print(f"  DEBUG: lista[{i}] = {elemento}")

print("\nVentajas:")
print("  ✅ Simple y rápido")
print("  ✅ No requiere herramientas adicionales")
print("  ✅ Funciona en cualquier entorno")

print("\nDesventajas:")
print("  ❌ Muchos prints pueden ser molestos")
print("  ❌ Hay que eliminarlos después")
print("  ❌ No es estructurado")

print("\n" + "=" * 50)
