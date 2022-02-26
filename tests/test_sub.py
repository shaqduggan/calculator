"""
Test the Subtraction of integers
"""
import unittest
from calculator import Calculator

class CalculatorSubtractTests(unittest.TestCase):
	"""
	Test the Subtraction of integers
	"""

	def test_subtraction_integers(self):
		"""
		Test the Subtraction of integers
		"""
		self.assertEqual(Calculator([10,5]).subtract(), 5)

	def test_subtraction_floats(self):
		"""
		Test the Subtraction of floats
		"""
		self.assertEqual(Calculator([10.0,7.5]).subtract(), 2.5)

if __name__ == '__main__':
    unittest.main()