import unittest
from calculator import Calculator

class CalculatorMedianTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_even_median(self):
        self.assertEqual(self.calc.median([10,1,9,7,5,1,3.2,2,6,4,8,9,4.8,2,3,1,5,10,3]), 4.8)

    def test_odd_median(self):
    	self.assertEqual(self.calc.median([1,2,3]), 2)

if __name__ == '__main__':
    unittest.main()