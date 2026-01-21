"""
TESTING: FIXTURES
=================
Configuración y limpieza en pruebas
"""

print("=" * 50)
print("FIXTURES - CONFIGURACIÓN")
print("=" * 50)

import unittest

class TestConFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Se ejecuta una vez antes de todas las pruebas"""
        print("\n  setUpClass() - Configuración de clase")
        cls.datos_compartidos = "Configuración compartida"
    
    @classmethod
    def tearDownClass(cls):
        """Se ejecuta una vez después de todas las pruebas"""
        print("  tearDownClass() - Limpieza de clase")
    
    def setUp(self):
        """Se ejecuta antes de cada prueba"""
        print("  setUp() - Configuración antes de cada prueba")
        self.lista = [1, 2, 3]
    
    def tearDown(self):
        """Se ejecuta después de cada prueba"""
        print("  tearDown() - Limpieza después de cada prueba")
    
    def test_operacion1(self):
        """Primera prueba"""
        print("    Ejecutando test_operacion1")
        self.assertEqual(len(self.lista), 3)
    
    def test_operacion2(self):
        """Segunda prueba"""
        print("    Ejecutando test_operacion2")
        self.assertIn(2, self.lista)

print("\nFixtures:")
print("  setUpClass() - Una vez antes de todas")
print("  tearDownClass() - Una vez después de todas")
print("  setUp() - Antes de cada prueba")
print("  tearDown() - Después de cada prueba")

print("\nEjemplo:")
print("  class TestConFixtures(unittest.TestCase):")
print("      def setUp(self):")
print("          self.lista = [1, 2, 3]")
print("")
print("      def test_algo(self):")
print("          self.assertEqual(len(self.lista), 3)")

# Ejecutar para mostrar el orden
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)

print("\nUso común:")
print("  - Configurar datos de prueba")
print("  - Crear objetos temporales")
print("  - Limpiar archivos temporales")
print("  - Cerrar conexiones")

print("\n" + "=" * 50)
