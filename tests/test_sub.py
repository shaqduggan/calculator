import unittest
from calculator import Calculator

class CalculatorSubtractTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_subtraction_integers(self):
		""" 
		Test the Subtraction of integers
		"""
		self.assertEqual(self.calc.subtract(10,5), 5)

	def test_subtraction_floats(self):
		""" 
		Test the Subtraction of floats
		"""
		self.assertEqual(self.calc.subtract(10.0,7.5), 2.5)

if __name__ == '__main__':
    unittest.main()