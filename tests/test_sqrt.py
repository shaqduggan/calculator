import unittest
from calculator import Calculator

class CalculatorSqrtTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_pos_square_root(self):
		""" 
		Test the squareroot
		"""
		self.assertEqual(self.calc.sqrt(4), 2)
		
if __name__ == '__main__':
    unittest.main()