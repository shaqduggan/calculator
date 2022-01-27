import unittest
from calculator import Calculator

class CalculatorAddTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_add_integers(self):
		""" 
		Test the addition of integers
		"""
		self.assertEqual(self.calc.add(2,3), 5)

	def test_add_floats(self):
		""" 
		Test the addition of floats
		"""
		self.assertEqual(self.calc.add(2.0,3.2), 5.2)

if __name__ == '__main__':
    unittest.main()
