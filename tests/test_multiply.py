"""
Test the multiplication of integers
"""
import unittest
from calculator import Calculator

class CalculatorMultiplyTests(unittest.TestCase):
	"""
	Test the multiplication of integers
	"""
	def test_multiply_integers(self):
		"""
		Test the multiplication of integers
		"""
		self.assertEqual(Calculator([2,3]).multiplication(), 6)

if __name__ == '__main__':
    unittest.main()
