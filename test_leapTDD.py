import unittest
import leapTDD

class TestCase(unittest.TestCase):

    #test one
    def test_leap(self):
        self.assertEqual(leapTDD.leap(4), "leap year")
    #test two
    def test_leap2(self):
        self.assertEqual(leapTDD.leap(5), "NOT a leap year")
    #test three
    def test_leap3(self):
        self.assertEqual(leapTDD.leap(40), "leap year")        
    #test four
    def test_leap4(self):
        self.assertEqual(leapTDD.leap(900), "NOT a leap year")        
    #test five
    def test_leap5(self):
        self.assertEqual(leapTDD.leap(800), "leap year")
    #test six
    def test_leap6(self):
        self.assertEqual(leapTDD.leap(1964), "leap year")        
   
if __name__ == '__main__':
    unittest.main()