import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):


	def test_add_integers(self):
		calc = Calculator()
		self.assertEqual(calc.add(2,3), 5)

	def test_add_floats(self):
		calc = Calculator()
		self.assertEqual(calc.add(2.0,3.2), 5.2)

if __name__ == '__main__':
    unittest.main()
