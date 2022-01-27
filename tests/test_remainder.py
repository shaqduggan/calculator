import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_remainder_integer(self):
        self.assertEqual(self.calc.remainder(7, 4), 3)
    
    def test_remainder_float(self):
        self.assertFalse(isinstance(self.calc.remainder(10, 0.3), int))

if __name__ == '__main__':
    unittest.main()