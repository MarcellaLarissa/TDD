import unittest
import fizzBuzz

class TestCase(unittest.TestCase):

    #test one
    def test_fizz(self):
        self.assertEqual(fizzBuzz.fb(1), 1)
    #test two
    def test_fizz2(self):
        self.assertEqual(fizzBuzz.fb(2), 2)
    #test three   
    def test_fizz3(self):
        self.assertEqual(fizzBuzz.fb(3), "fizz")
    #test four   
    def test_fizz4(self):
        self.assertEqual(fizzBuzz.fb(5), "buzz")
    #test five   
    def test_fizz5(self):
        self.assertEqual(fizzBuzz.fb(15), "fizzbuzz")
   #test six   
    def test_fizz5(self):
        self.assertEqual(fizzBuzz.fb(101), None)     
if __name__ == '__main__':
    unittest.main()