import unittest
from calculator import Calculator

class CalculatorMultiplyTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_multiply_integers(self):
		""" 
		Test the multiplication of integers
		"""
		self.assertEqual(self.calc.multiplication(2,3), 6)

if __name__ == '__main__':
    unittest.main()
