import unittest

# here we are creating our own new class 
# that inherits from unittest.TestCase called TestStringMethods
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper()) #assert the answer will be true
        self.assertFalse('Foo'.isupper()) # assert the answer will be false

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world']) # assert the answer will be equal
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main() 