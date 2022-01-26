import unittest
from calculator_funcs import Calculator

class CalculatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_add_integers(self):
        self.assertEqual(self.calc.add(2,3), 5)
    
    def test_add_float(self):
        self.assertEqual(self.calc.add(3.2, 1.2), 4.4)

if __name__ == '__main__':
    unittest.main()