"""
RESUMEN: TESTING
================
Todas las técnicas de testing
"""

print("=" * 50)
print("RESUMEN - TESTING")
print("=" * 50)

print("\nConcepto:")
print("  - Verificar que el código funciona")
print("  - Pruebas automatizadas")
print("  - Detectar errores temprano")

print("\nBibliotecas:")
print("  unittest - Incluido en Python")
print("  pytest - Popular y potente")
print("  assert - Pruebas simples")

print("\nUnittest:")
print("  import unittest")
print("")
print("  class TestMiFuncion(unittest.TestCase):")
print("      def test_algo(self):")
print("          self.assertEqual(func(), esperado)")

print("\nAssertions:")
print("  self.assertEqual(a, b)")
print("  self.assertNotEqual(a, b)")
print("  self.assertTrue(x)")
print("  self.assertFalse(x)")
print("  self.assertIn(item, list)")
print("  self.assertRaises(Error)")

print("\nFixtures:")
print("  setUp() - Antes de cada prueba")
print("  tearDown() - Después de cada prueba")
print("  setUpClass() - Una vez antes de todas")
print("  tearDownClass() - Una vez después de todas")

print("\nMocks:")
print("  from unittest.mock import Mock, patch")
print("  mock = Mock()")
print("  mock.metodo.return_value = valor")
print("  with patch('modulo.funcion') as mock:")

print("\nEjecutar:")
print("  python -m unittest test_archivo.py")
print("  pytest test_archivo.py")

print("\nVentajas:")
print("  ✅ Confianza en el código")
print("  ✅ Detectar errores temprano")
print("  ✅ Documentación del comportamiento")
print("  ✅ Facilitar refactorización")

print("\n" + "=" * 50)
