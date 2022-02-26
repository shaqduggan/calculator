"""
Test for finding median
"""
import unittest
from calculator import Calculator

class CalculatorMedianTests(unittest.TestCase):
    """
    Test for finding median
    """

    def test_even_median(self):
        """
        Test for finding median in an even number list
        """
        self.assertEqual(Calculator([10,1,9,7,5,1,3.2,2,6,4,8,9,4.8,2,3,1,5,10,3]).median(), 4.8)

    def test_odd_median(self):
        """
        Test for finding median in an odd number list
        """
        self.assertEqual(Calculator([1,2,3]).median(), 2)

if __name__ == '__main__':
    unittest.main()