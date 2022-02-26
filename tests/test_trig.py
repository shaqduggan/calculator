"""
Test for sine, cosine, and tangent
"""
import unittest
from calculator import Calculator

class CalculatorTrigTests(unittest.TestCase):
	"""
	Test for sine, cosine, and tangent
	"""

	def test_sine(self):
		"""
		Test for sine
		"""
		self.assertEqual(round(Calculator([2]).sine(),2), 0.91)

	def test_cosine(self):
		"""
		Test for cosine
		"""
		self.assertEqual(round(Calculator([2]).cosine(),2), -0.42)

	def test_tangent(self):
		"""
		Test tangent
		"""
		self.assertEqual(round(Calculator([2]).tangent(),2), -2.19)

if __name__ == '__main__':
    unittest.main()