import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_add_integers(self):
		""" 
		Test the addition of integers
		"""
		self.assertEqual(self.calc.add(2,3), 5)

	def test_add_floats(self):
		""" 
		Test the addition of floats
		"""
		self.assertEqual(self.calc.add(2.0,3.2), 5.2)
	
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