"""
TESTING: MOCKS
==============
Simular objetos y funciones
"""

print("=" * 50)
print("MOCKS - SIMULAR OBJETOS")
print("=" * 50)

from unittest.mock import Mock, patch, MagicMock

print("\nMocks:")
print("  - Simular objetos y funciones")
print("  - Aislar código bajo prueba")
print("  - Controlar comportamiento")

# Mock básico
print("\nMock básico:")
mock = Mock()
mock.metodo.return_value = 42
print(f"  mock.metodo() = {mock.metodo()}")
print(f"  mock.metodo() = {mock.metodo()}")

# Verificar llamadas
print("\nVerificar llamadas:")
mock.metodo("arg1", "arg2")
mock.metodo.assert_called_once()
mock.metodo.assert_called_with("arg1", "arg2")
print("  ✅ Llamadas verificadas")

# Mock con patch
print("\nMock con patch:")
def obtener_fecha():
    from datetime import datetime
    return datetime.now()

with patch('__main__.obtener_fecha') as mock_fecha:
    mock_fecha.return_value = "2024-01-01"
    resultado = obtener_fecha()
    print(f"  obtener_fecha() = {resultado}")

# MagicMock
print("\nMagicMock:")
magic_mock = MagicMock()
magic_mock.__len__.return_value = 5
print(f"  len(magic_mock) = {len(magic_mock)}")

print("\nUsos:")
print("  ✅ Simular llamadas a API")
print("  ✅ Simular base de datos")
print("  ✅ Simular archivos")
print("  ✅ Aislar dependencias")

print("\nVentajas:")
print("  ✅ Controlar comportamiento")
print("  ✅ Aislar código")
print("  ✅ Pruebas más rápidas")
print("  ✅ No depende de recursos externos")

print("\n" + "=" * 50)
