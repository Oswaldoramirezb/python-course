"""
TESTING: UNITTEST
=================
Usar unittest para pruebas
"""

print("=" * 50)
print("UNITTEST")
print("=" * 50)

import unittest

# Función a probar
def sumar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

# Clase de pruebas
class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        """Probar función sumar"""
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)
    
    def test_dividir(self):
        """Probar función dividir"""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
    
    def test_dividir_por_cero(self):
        """Probar división por cero"""
        with self.assertRaises(ValueError):
            dividir(10, 0)

print("\nCrear clase de pruebas:")
print("  class TestOperaciones(unittest.TestCase):")
print("      def test_sumar(self):")
print("          self.assertEqual(sumar(2, 3), 5)")

print("\nAssertions comunes:")
print("  self.assertEqual(a, b) - a == b")
print("  self.assertNotEqual(a, b) - a != b")
print("  self.assertTrue(x) - x es True")
print("  self.assertFalse(x) - x es False")
print("  self.assertIn(item, list) - item en list")
print("  self.assertRaises(Error) - Lanza error")

print("\nEjecutar:")
print("  python -m unittest test_archivo.py")
print("  python -m unittest -v  # Verbose")

# Ejecutar pruebas
if __name__ == '__main__':
    unittest.main(verbosity=2)

print("\n" + "=" * 50)
