import unittest
from calculator import Calculator

class CalculatorAddTests(unittest.TestCase):


	def test_add_integers(self):
		"""
		Test the addition of integers
		"""
		self.assertEqual(Calculator([2,3]).add(), 5)

	def test_add_floats(self):
		"""
		Test the addition of floats
		"""
		self.assertEqual(Calculator([2.0,3.2]).add(), 5.2)

if __name__ == '__main__':
    unittest.main()
