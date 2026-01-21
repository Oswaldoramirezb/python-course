"""
TYPE HINTS: EN FUNCIONES
========================
Anotaciones de tipo en funciones
"""

print("=" * 50)
print("TYPE HINTS EN FUNCIONES")
print("=" * 50)

# Función con type hints
def calcular_promedio(notas: list[float]) -> float:
    """Calcula el promedio de notas"""
    return sum(notas) / len(notas)

print("\nFunción con lista:")
print("  def calcular_promedio(notas: list[float]) -> float:")
notas = [85.5, 90.0, 78.5]
print(f"  calcular_promedio({notas}) = {calcular_promedio(notas):.2f}")

# Función con diccionario
def obtener_nombre(persona: dict[str, str]) -> str:
    """Obtiene el nombre de un diccionario"""
    return persona.get("nombre", "Desconocido")

print("\nFunción con diccionario:")
print("  def obtener_nombre(persona: dict[str, str]) -> str:")
persona = {"nombre": "Juan", "ciudad": "Madrid"}
print(f"  obtener_nombre({persona}) = {obtener_nombre(persona)}")

# Función con Optional
from typing import Optional

def buscar_elemento(lista: list[int], elemento: int) -> Optional[int]:
    """Busca elemento y retorna índice o None"""
    if elemento in lista:
        return lista.index(elemento)
    return None

print("\nFunción con Optional:")
print("  from typing import Optional")
print("  def buscar_elemento(...) -> Optional[int]:")
print(f"  buscar_elemento([1,2,3], 2) = {buscar_elemento([1,2,3], 2)}")
print(f"  buscar_elemento([1,2,3], 5) = {buscar_elemento([1,2,3], 5)}")

print("\n" + "=" * 50)
