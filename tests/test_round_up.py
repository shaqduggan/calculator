import unittest
from calculator import Calculator

class CalculatorRoundUpTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_round_up_floats(self):
		""" 
		Test the round up of floats
		"""
		self.assertEqual(self.calc.round_up(5.5,0), 6.0)

if __name__ == '__main__':
    unittest.main()
