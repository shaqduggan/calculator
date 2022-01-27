import unittest
from calculator import Calculator


class CalculatorIsPrimeTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.calc = Calculator()

	def test_is_prime(self):
		""" 
		Test the addition of integers
		"""
		self.assertTrue(self.calc.isPrime(2))
		self.assertTrue(self.calc.isPrime(5))

	def test_is_not_prime(self):

		self.assertFalse(self.calc.isPrime(4))
		self.assertFalse(self.calc.isPrime(8))
