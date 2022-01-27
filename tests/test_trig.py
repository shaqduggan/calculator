import unittest
from calculator import Calculator

class CalculatorTrigTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_sine(self):
		""" 
		Test for sine
		"""
		self.assertEqual(round(self.calc.sine(2),2), 0.91)
	
	def test_cosine(self):
		""" 
		Test for cosine
		"""
		self.assertEqual(round(self.calc.cosine(2),2), -0.42)
	
	def test_tangent(self):
		""" 
		Test tangent
		"""
		self.assertEqual(round(self.calc.tangent(2),2), -2.19)
	

if __name__ == '__main__':
    unittest.main()