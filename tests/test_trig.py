import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

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
		self.assertEqual(self.calc.sin(2), 0.9092974268256817)
	
	def test_cosine(self):
		""" 
		Test for cosine
		"""
		self.assertEqual(self.calc.sin(2), -0.4161468365471424)
	
	def test_tangent(self):
		""" 
		Test tangent
		"""
		self.assertEqual(self.calc.sin(2), -2.185039863261519)
	

if __name__ == '__main__':
    unittest.main()