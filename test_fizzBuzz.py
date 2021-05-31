import unittest
import fizzBuzz

class TestCase(unittest.TestCase):

    #test one
    def test_leap(self):
        self.assertEqual(fizzBuzz.nums(1), 1)
        
if __name__ == '__main__':
    unittest.main()