import unittest
from calculator import Calculator


class CalculatorIsPrimeTests(unittest.TestCase):

	def test_is_prime(self):
		"""
		Test if a number is prime 
		"""
		self.assertTrue(Calculator([2]).is_prime())
		self.assertTrue(Calculator([5]).is_prime())

	def test_is_not_prime(self):
		"""
		Test if a number is not prime
		"""
		self.assertFalse(Calculator([4]).is_prime())
		self.assertFalse(Calculator([8]).is_prime())
