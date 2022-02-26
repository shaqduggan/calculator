"""
Test the squareroot
"""
import unittest
from calculator import Calculator

class CalculatorSqrtTests(unittest.TestCase):
	"""
	Test the squareroot
	"""
	def test_pos_square_root(self):
		"""
		Test the squareroot
		"""
		self.assertEqual(Calculator([4]).sqrt(), 2)

if __name__ == '__main__':
    unittest.main()