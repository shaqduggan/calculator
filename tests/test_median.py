import unittest
from calculator_exercise import Calculator

class CalculatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_median(self):
        self.assertEqual(self.calc.median([10,1,9,7,5,1,3.2,2,6,4,8,9,4.8,2,3,1,5,10,3]), 4.8)

if __name__ == '__main__':
    unittest.main()