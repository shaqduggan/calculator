import unittest
from calculator import Calculator

class CalculatorRoundUpTests(unittest.TestCase):

	def test_round_up_floats(self):
		"""
		Test the round up of floats
		"""
		self.assertEqual(Calculator([5.5557,2]).round_up(), 5.56)

if __name__ == '__main__':
    unittest.main()
