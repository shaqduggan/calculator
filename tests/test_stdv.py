import unittest
import statistics
from calculator import Calculator

class CalculatorStdvTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_stdv(self):
        """ tests if the functuon returns stdv value as expected """
        self.assertEqual(self.calc.stdv([10,1,9,7,5,1,3.2,2,6,4,8,9,4.8,2,3,1,5,10,3]), 3.1112)

    def test_stdv_against_stat_lib(self):
        """ comapare returned value from calc.stdv to the equivalence of stats lib (both rounded at 4th decimal)"""
        self.assertEqual(self.calc.stdv([10,1,9,7,5,1,3.2,2,6,4,8,9,4.8,2,3,1,5,10,3]), round(statistics.stdev([10,1,9,7,5,1,3.2,2,6,4,8,9,4.8,2,3,1,5,10,3]), 4))

if __name__ == '__main__':
    unittest.main()