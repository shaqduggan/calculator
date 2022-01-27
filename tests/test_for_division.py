import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_division_integers(self):
		""" 
		Test the division of integers
		"""
		self.assertEqual(self.calc.division(6,3), 2)

	def test_division_floats(self):
		""" 
		Test the division of floats  
		"""
		self.assertEqual(self.calc.division(4.4,2.2), 2)

if __name__ == '__main__':
    unittest.main()