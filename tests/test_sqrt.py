import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_squareroot(self):
		""" 
		Test the squareroot
		"""
		self.assertEqual(self.calc.sqrt(4), 2)

if __name__ == '__main__':
    unittest.main()