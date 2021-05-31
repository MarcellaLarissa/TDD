import unittest
import leapTDD

class TestCase(unittest.TestCase):

    #test one
    def test_leap(self):
        self.assertEqual(leapTDD.leap(4), "leap year")
    #test one
    def test_leap2(self):
        self.assertEqual(leapTDD.leap(5), "NOT a leap year")
        

        
   
if __name__ == '__main__':
    unittest.main()