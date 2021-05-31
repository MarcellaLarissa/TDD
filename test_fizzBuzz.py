import unittest
import fizzBuzz

class TestCase(unittest.TestCase):

    #test one
    def test_leap(self):
        self.assertEqual(fizzBuzz.nums(1), 1)
    #test two
    def test_leap2(self):
        self.assertEqual(fizzBuzz.nums(1), 2)
        
if __name__ == '__main__':
    unittest.main()